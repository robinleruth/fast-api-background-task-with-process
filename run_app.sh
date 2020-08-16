#!/bin/bash

export APP_ENV=prd

echo "Create virtual env"

python -m venv venv

source venv/bin/activate

echo "Install requirements"

python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Run redis & run celery"
# ./run-redis.sh

echo "Run celery"
# celery worker -A app.infrastructure.celery --loglevel=info & # -S worker_state_db &

echo "Run flower"
# celery flower -A app.infrastructure.celery --adress=127.0.0.1 --port=5555 &


echo "Launch API"
python api.py
