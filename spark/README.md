## Blog post

[Spark SQL Editor](https://medium.com/data-querying/a-sparksql-editor-via-hue-and-the-spark-sql-server-f82e72bbdfc7)


## One-line setup

For fetching the configurations and starting everything:

    mkdir spark
    cd spark
    wget https://raw.githubusercontent.com/romainr/query-demo/master/spark/docker-compose.yml


    docker-compose up -d

Then those URLs will be up:

* [http://localhost:8888/](http://localhost:8888/) Hue Editor
* [http://127.0.0.1:8080/](http://127.0.0.1:8080/) Spark Master Web UI
* [http://127.0.0.1:4040/environment/](http://127.0.0.1:4040/environment/) Thrift SQL UI
* [http://127.0.0.1:7070](http://127.0.0.1:7070) Spark Master
* [http://localhost:8998](http://localhost:8998) Livy REST Server


For stopping everything:

    docker-compose down
