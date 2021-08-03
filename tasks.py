from src.marketData.DataManager import datamanager
from src.database.Schemas import RobotSchema
from src.database.Parsers import getRobotFromSchema
from bson import ObjectId
from celery import Celery

app = Celery('src', broker='pyamqp://guest@localhost//', include=['src'])


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


