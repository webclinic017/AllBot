from celery import Celery
from database import BackTestSchema
from ManagerBacktest import generateStats
from datetime import date


app = Celery('tasks', broker='redis://:Sg2oKCcsul4L6yJdgunwM6JP7MPiSXYP@redis-12481.c270.us-east-1-3.ec2.cloud.redislabs.com:12481/0')

@app.task()
def runAllBacktests():
    backTest = BackTestSchema()
    backTest.stats = generateStats()
    backTest.date = date.today()
    backTest.save()



