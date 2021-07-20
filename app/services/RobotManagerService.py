from app.marketData.DataManager import datamanager
from app.services.RobotService import *
from app.utils.message import *


def startRobot(data):
    robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
    if robot and (str(robot.owner) == data['owner']):
        datamanager.addObserver(IFR2FromSchema(robot))
        return SUCCESS_START, 200
    else:
        return ERROR_START, 400


def stopRobot(data):
    robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
    if robot and (str(robot.owner) == data['owner']) and datamanager.removeObserver(robot):
        return SUCCESS_STOP, 200
    return ERROR_STOP, 400


