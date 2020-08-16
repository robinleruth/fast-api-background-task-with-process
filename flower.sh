source venv/bin/activate
export APP_ENV=prd
celery flower -A app.infrastructure.celery --adress=127.0.0.1 --port=5555 
