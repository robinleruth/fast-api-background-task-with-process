source venv/bin/activate
export APP_ENV=prd
celery worker -A app.infrastructure.celery --loglevel=info  -S worker_state_db
