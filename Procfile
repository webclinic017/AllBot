web: gunicorn wsgi:app
worker: celery -A worker worker -l debug -Q backtest
