#!/usr/bin/env python
# -- coding: utf-8 --
# Copyright 2023 Romain Rigaux
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mlflow.pyfunc
import pandas
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer


class Sentiment(mlflow.pyfunc.PythonModel):
    # https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "distilbert-base-uncased-finetuned-sst-2-english"
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "distilbert-base-uncased-finetuned-sst-2-english"
        )

    def predict(self, context, model_input):
        if "text" in model_input:
            # Pandas
            if type(model_input["text"]) == str:
                input = [model_input["text"]]
            else:
                input = model_input["text"].astype(str).values.tolist()
        else:
            # Getting '0' as column name in SparkSql
            input = model_input["0"].iloc[0]
        return self.get_sentiment(input)

    def get_sentiment(self, input):
        inputs = self.tokenizer(input, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits

        predicted_class_id = logits.argmax().item()

        return pandas.DataFrame([self.model.config.id2label[predicted_class_id]])


with mlflow.start_run(run_name="sentiment") as run:
    python_model = Sentiment()

    print("%s model" % python_model.model)

    mlflow.pyfunc.log_model("model", python_model=python_model)
