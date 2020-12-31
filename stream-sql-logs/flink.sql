
-- Mapping Topic data to a Table
CREATE TABLE hue_logs (
  log STRING,
  proctime AS PROCTIME()
) WITH (
  'connector' = 'kafka',
  'topic' = 'hue_logs',
  'properties.bootstrap.servers' = 'kafka:9094',
  'format' = 'json'
);

-- Fiddling with functions
SELECT
  REGEXP_EXTRACT('[31/Dec/2020 06:02:36 -0800] access INFO 172.26.0.1 romain - "POST /notebook/api/check_status HTTP/1.1" returned in 45ms 200 276', '\[([^ ]+ [^ ]+).*', 1) as dt
;

-- Extracting some of the fields
SELECT
  REGEXP_EXTRACT(log, '\[([^ ]+ [^ ]+).*', 1) as dt,
  REGEXP_EXTRACT(log, '.*access\s+([^ ]+)\s+([^ ]+)\s+([^ ]+)\s+\-.*', 3) as username,
  log
FROM hue_logs
LIMIT 100
;

-- Live counts of API calls made per user
SELECT
  username,
  count(*) as callsCt
FROM (
  SELECT REGEXP_EXTRACT(log, '.*access\s+([^ ]+)\s+([^ ]+)\s+([^ ]+)\s+\-.*', 3) as username
  FROM hue_logs
)
GROUP BY username
;

-- Table for outputting calculations to a new Topic
CREATE TABLE hue_stats (
  ts TIMESTAMP(3),
  -- ts bigint, -- Depends if using `SECOND()` in `TUMBLE` or not
  username STRING,
  callsCt BIGINT,
  PRIMARY KEY (username, ts) NOT ENFORCED
) WITH (
  'connector' = 'upsert-kafka',
  'topic' = 'hue_stats',
  'properties.bootstrap.servers' = 'kafka:9094',
  'key.format' = 'json',
  'value.format' = 'json'
);

-- INSERT into hue_stats -- Uncomment to send to the Topic after creating the `hue_stats` table below
-- Rolling windows of aggregation
SELECT
  TUMBLE_START(proctime, INTERVAL '10' SECOND) as ts,
  username,
  COUNT(*) as callsCt
FROM (
  SELECT
    REGEXP_EXTRACT(log, '.*access\s+([^ ]+)\s+([^ ]+)\s+([^ ]+)\s+\-.*', 3) as username, proctime
    FROM hue_logs
  )
GROUP BY TUMBLE(proctime, INTERVAL '10' SECOND), username
;

-- Poke at the generated stats
SELECT *
FROM hue_stats
LIMIT 100
;
