## Blog post

[Live Querying live Logs and Sending live Updates easily](https://medium.com/data-querying/live-sql-querying-live-logs-and-sending-live-updates-easily-e6297150cf92)

## One-line setup

For fetching the configurations and starting everything:

    mkdir stream-sql-demo
    cd stream-sql-demo
    wget https://raw.githubusercontent.com/romainr/query-demo/master/stream-sql-demo/docker-compose.yml


    docker-compose up -d
    >
    Creating network "stream-sql-logs_default" with the default driver
    Creating stream-sql-logs_fluentd_1     ... done
    Creating stream-sql-logs_zookeeper_1   ... done
    Creating hue-database                  ... done
    Creating ksqldb-server                 ... done
    Creating stream-sql-logs_jobmanager_1 ... done
    Creating stream-sql-logs_taskmanager_1 ... done
    Creating flink-sql-api                 ... done
    Creating hue                           ... done
    Creating stream-sql-logs_kafka_1       ... done


Then those URLs will be up:

* [http://localhost:8888/](http://localhost:8888/) Hue Editor
* [http://localhost:8081/](http://localhost:8081/) Flink Dashboard

As well as the Flink SQL Gateway and ksqlDB APIs:

    curl localhost:8083/v1/info
    > {"product_name":"Apache Flink","version":"1.12.0"}

    curl http://localhost:8088/info
    > {"KsqlServerInfo":{"version":"0.12.0","kafkaClusterId":"DJzUX-zaTDCC5lqfVwf8kw","ksqlServiceId":"default_","serverStatus":"RUNNING"}}

For stopping everything:

    docker-compose down

## SQL

### Flink SQL

https://gist.github.com/romainr/dc5087f26c3bcaf90906b83c489f2413

### ksqlDB

https://gist.github.com/romainr/fff457cd69d7328cce8652e93f555692
