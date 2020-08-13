#!/bin/bash

python -m venv venv

source venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

export APP_ENV=prd

echo "Launch API"
python api.py
