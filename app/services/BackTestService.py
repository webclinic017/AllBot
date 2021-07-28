from app.database.Schemas import RobotSchema, BackTestSchema
from app.backtest.ManagerBacktest import getBacktest, generateStats
from app.utils.Message import *
from flask import jsonify
from bson import ObjectId
from datetime import date


def getOneBackTest(data):
    try:
        robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
        if robot and (str(robot.owner) == data['owner']):
            return getBacktest(robot), 200
        else:
            return ERROR_START, 400
    except:
        return RESOURCE_NOT_FOUND, 400


def getAllBackTest(data):
    try:
        backtest = BackTestSchema.objects(date=date.today()).first()
        print(backtest)
        if backtest:
            return jsonify(backtest), 200
        backtests = generateStats()
        if backtests:
            bt = BackTestSchema()
            bt.date = date.today()
            bt.stats = backtests
            return jsonify(bt.save().to_json()), 200
    except:
        return RESOURCE_NOT_FOUND, 400





