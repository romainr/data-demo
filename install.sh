#!/usr/bin/env bash

if [ "$(uname)" == "Darwin" ]
then
  brew install python3 # mysql redis
  pip3 install virtualenv
  virtualenv -p python3 python_env
else
  sudo apt-get update

  sudo apt-get install python3-pip python3.8-venv -y

  sudo pip3 install virtualenv
  python3.8 -m venv python_env
fi

source python_env/bin/activate

pip install -r requirements.txt
