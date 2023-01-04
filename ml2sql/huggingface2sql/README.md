
# Huggingface2SQL

This is a project to train a model to convert natural language to SQL queries. The model is based on the Huggingface Transformers. The model is applied to data directly in SQL via a SparkSql UDF.

Install dependencies:
```
pip install -r requirements.txt
```

Launch UIs:
```
mlflow ui
jupyter-lab
```

Train Model:
```
python ml2sql/huggingface2sql/text2sql_model_train.py
```
