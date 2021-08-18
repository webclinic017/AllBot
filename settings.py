import os

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
MONGO_URI = os.environ.get('MONGO_URI')
DB = os.environ.get('DB')


MONGO_URI="mongodb+srv://dev:groselha24@allbot.poydz.mongodb.net/Bots?retryWrites=true&w=majority"
DB="Bots"
CELERY_BROKER_URL="redis://:Sg2oKCcsul4L6yJdgunwM6JP7MPiSXYP@redis-12481.c270.us-east-1-3.ec2.cloud.redislabs.com:12481/0"
