#! /bin/bash

sudo apt install python3 python3-pip python3-venv -y

python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt

pytest --cov ./frontend/app.py --cov-report term-missing
pytest --cov ./backend/application --cov-report term-missing

deactivate
rm -rf venv