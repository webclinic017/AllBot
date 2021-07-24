from app.database.Schemas import RobotSchema
from app.backtest.ManagerBacktest import getBacktest
from app.utils.message import *
from bson import ObjectId


def getOneBackTest(data):
    try:
        robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
        if robot:
            return getBacktest(robot), 200
        else:
            return ERROR_START, 400
    except:
        return RESOURCE_NOT_FOUND, 400





