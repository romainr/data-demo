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
import pandas
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class TextToSql(mlflow.pyfunc.PythonModel):
    # https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html

    def __init__(self, size="small"):
        self.name = "mrm8488/t5-%s-finetuned-wikiSQL" % size
        self.tokenizer = AutoTokenizer.from_pretrained(self.name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.name)

    def predict(self, context, model_input):
        if "text" in model_input:
            input = model_input["text"]
        else:
            # Getting '0' as column name in SparkSql
            #         model_input :                            0
            # 0  number of carrots in 2022
            input = model_input["0"].iloc[0]
        return self.get_sql(input)

    def get_sql(self, query):
        input_text = "translate English to SQL: %s </s>" % query
        features = self.tokenizer([input_text], return_tensors="pt")

        output = self.model.generate(
            input_ids=features["input_ids"], attention_mask=features["attention_mask"]
        )

        return pandas.DataFrame(
            [
                self.tokenizer.decode(output[0])
                .replace("<pad> ", "", 1)
                .replace("</s>", "")
            ]
        )


with mlflow.start_run(run_name="text2sql") as run:
    size = "small"  # small/base
    python_model = TextToSql(size=size)

    print("%s model" % python_model.name)
    mlflow.log_param("size", size)

    mlflow.pyfunc.log_model("model", python_model=python_model)
