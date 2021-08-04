from src.marketData.DataManager import datamanager
from src.database.Schemas import RobotSchema
from src.database.Parsers import getRobotFromSchema
from src.database.Connection import connection
from bson import ObjectId
from celery import Celery

app = Celery('tasks', broker='redis://:Sg2oKCcsul4L6yJdgunwM6JP7MPiSXYP@redis-12481.c270.us-east-1-3.ec2.cloud.redislabs.com:12481/0')

@app.task()
def startRobot(id):
    robot = RobotSchema.objects(id=ObjectId(id)).first()
    print(robot)
    if robot:
        datamanager.addObserver(getRobotFromSchema(robot))
        print(len(datamanager.observers))


@app.task()
def stopRobot(id):
    datamanager.removeObserver(id)




