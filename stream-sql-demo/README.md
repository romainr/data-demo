## One-line setup

For fetching the configurations and starting everything:

    mkdir stream-sql-demo
    cd stream-sql-demo
    wget https://raw.githubusercontent.com/romainr/query-demo/master/stream-sql-demo/docker-compose.yml


    docker-compose up -d
    >
    Creating network "stream-sql-demo_default" with the default driver
    Creating hue-database                  ... done
    Creating stream-sql-demo_jobmanager_1 ... done
    Creating stream-sql-demo_mysql_1       ... done
    Creating ksqldb-server                 ... done
    Creating stream-sql-demo_zookeeper_1   ... done
    Creating flink-sql-api                 ... done
    Creating stream-sql-demo_taskmanager_1 ... done
    Creating hue                           ... done
    Creating ksqldb-cli                    ... done
    Creating stream-sql-demo_kafka_1       ... done
    Creating stream-sql-demo_datagen_1     ... done


Then those URLs will be up:

* [http://localhost:8888/](http://localhost:8888/) Hue Editor
* [http://localhost:8081/](http://localhost:8081/) Flink Dashboard

As well as the Flink SQL Gateway and ksqlDB APIs:

    curl localhost:8083/v1/info
    > {"product_name":"Apache Flink","version":"1.11.1"}

    curl http://localhost:8088/info
    > {"KsqlServerInfo":{"version":"0.12.0","kafkaClusterId":"DJzUX-zaTDCC5lqfVwf8kw","ksqlServiceId":"default_","serverStatus":"RUNNING"}}

For stopping everything:

    docker-compose down
