export APP_ENV=test

source venv/bin/activate

clear
# python -m unittest discover
python -m unittest tests/test_cache_service.py
