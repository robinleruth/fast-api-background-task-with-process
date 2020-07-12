#!/bin/bash

source venv/bin/activate

export APP_ENV=prd

echo "Launch API"
python api.py
