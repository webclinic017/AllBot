import os

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
MONGO_URI = os.environ.get('MONGO_URI')
DB = os.environ.get('DB')
