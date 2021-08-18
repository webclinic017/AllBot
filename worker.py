from src.marketData.DataManager import datamanager
from src.database.Schemas import RobotSchema
from src.database.Parsers import getRobotFromSchema
from src.database.Connection import connection
from settings import CELERY_BROKER_URL
from src.mobileNotify.SendNotify import message
from bson import ObjectId
from celery import Celery

print(CELERY_BROKER_URL)
app = Celery('tasks', broker=CELERY_BROKER_URL)


@app.task()
def startRobot(id):
    robot = RobotSchema.objects(id=ObjectId(id)).first()
    if robot:
        datamanager.addObserver(getRobotFromSchema(robot))
        robot.status = 'active'
        robot.save()
        message('Robô' + robot.nickName + ' ativado')


@app.task()
def stopRobot(id):
    robot = RobotSchema.objects(id=ObjectId(id)).first()
    if robot:
        datamanager.removeObserver(id)
        robot.status = 'inactive'
        robot.save()
        message('Robô' + robot.nickName + ' desativado')

