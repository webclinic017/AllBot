from app.marketData.DataManager import datamanager
from app.services.RobotService import *
from app.utils.Message import *


def startRobot(data):
    robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
    if robot and (str(robot.owner) == data['owner']):
        datamanager.addObserver(getRobotFromSchema(robot))
        return SUCCESS_START, 200
    else:
        return ERROR_START, 400


def stopRobot(data):
    robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
    if robot and (str(robot.owner) == data['owner']) and datamanager.removeObserver(getRobotFromSchema(robot)):
        return SUCCESS_STOP, 200
    return ERROR_STOP, 400


