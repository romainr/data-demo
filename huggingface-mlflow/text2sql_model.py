#!/usr/bin/env python

# -- coding: utf-8 --
# Copyright 2020 Romain Rigaux
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
from transformers import AutoModelWithLMHead, AutoTokenizer


class TextToSql(mlflow.pyfunc.PythonModel):
    def __init__(self, size="small"):
        name = "mrm8488/t5-%s-finetuned-wikiSQL" % size
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.model = AutoModelWithLMHead.from_pretrained(name)

    def predict(self, context, model_input):
        return self.get_sql(model_input["text"])

    def get_sql(self, query):
        input_text = "translate English to SQL: %s </s>" % query
        features = self.tokenizer([input_text], return_tensors="pt")

        output = self.model.generate(
            input_ids=features["input_ids"], attention_mask=features["attention_mask"]
        )

        return (
            self.tokenizer.decode(output[0])
            .replace("<pad> ", "", 1)
            .replace("</s>", "")
        )


def train(size="small"):
    with mlflow.start_run(run_name="text2sql") as run:
        python_model = TextToSql(size=size)

        print(
            "%s model (size=%s)"
            % (
                python_model,
                size,
            )
        )
        mlflow.log_param("size", size)

        mlflow.pyfunc.log_model("model", python_model=python_model)


def predict(query: str = "How many people live in the USA?", size: str = "small"):
    return TextToSql(size).predict(None, {"text": query})


if __name__ == "__main__":
    train()
