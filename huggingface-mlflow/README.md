

Train the model:

    python text2sql.py train

Query the model:

    python text2sql.py predict --query="How many people live in the USA?"

Serve the model:

    mlflow models serve -m /home/romain/projects/romain/text2sql/mlruns/0/efec45c930714e3581033699e011df51/artifacts/model -p 5001

    curl -X POST -H "Content-Type:application/json; format=pandas-split" --data '{"columns":["text"],"data":[["How many people live in the USA?"]]}' http://127.0.0.1:5001/invocations
    "SELECT COUNT Live FROM table WHERE Country = united states AND Name: text"
