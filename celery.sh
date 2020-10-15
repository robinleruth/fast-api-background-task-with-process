#!/bin/bash

source venv/bin/activate

export APP_ENV=prd

celery worker -A app.infrastructure.celery --loglevel=info -S worker_state_db -Q default,low_priority,high_priority
# celery worker -A app.infrastructure.celery --loglevel=info -Q default -c 2
# celery worker -A app.infrastructure.celery --loglevel=info -Q low_priority -c 1
# celery worker -A app.infrastructure.celery --loglevel=info -Q high_priority -c 4
