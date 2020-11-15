## Blog post

[Phoenix brings SQL to HBase and let you query Kafka data streams](https://medium.com/data-querying/phoenix-brings-sql-to-hbase-and-let-you-query-kafka-data-streams-8fd2edda1401)


## One-line setup

For fetching the configurations and starting everything:

    mkdir big-table-hbase
    cd big-table-hbase
    wget https://raw.githubusercontent.com/romainr/query-demo/master/big-table-hbase/docker-compose.yml


    docker-compose up -d

Then those URLs will be up:

* [http://localhost:8888/](http://localhost:8888/) Hue Editor
* [http://localhost:8765/](http://localhost:8765/)  Phoenix Query Server


http://localhost:8888/ Hue Editor


For stopping everything:

    docker-compose down
