
SHOW TOPICS;

CREATE STREAM hue_logs (
  log STRING
) WITH (
  kafka_topic='hue_logs',
  value_format='json',
  partitions=1
)
;

SELECT
  log,
  rowtime
FROM
  hue_logs
EMIT CHANGES
LIMIT 10
;

CREATE STREAM hue_stats (
  ts string,
  username STRING,
  callsCt BIGINT
) WITH (
  kafka_topic='hue_stats',
  value_format='json',
  partitions=1
)
;

SELECT
  *
FROM
  hue_stats
EMIT CHANGES
LIMIT 10
;
