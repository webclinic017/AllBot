from robots.ManagerRobots import DataManager
from robots.RobotUtils import createRobotFromJson
from flask import Blueprint, request
from roteamento.OrderSend import *

import json

managerRobots_blueprint = Blueprint('managerRobots_blueprint', __name__)

manager = None


@managerRobots_blueprint.route('/manager/play', methods=['GET'])
def Play():
    global manager
    robot = createRobotFromJson(json.loads(request.data))
    if robot:
        if manager is None:
            manager = DataManager("C:\Program Files\MetaTrader 5\\terminal64.exe", 50498337, "Pkvxcav9")
            '''manager = DataManager(session['userPreferences']['path'],
                                  session['userPreferences']['login'],
                                  session['userPreferences']['password'])'''
        manager.addObserver(robot)
        if not manager.is_alive():
            manager.start()
        return {"Sucesso": "Sucesso"}, 200
    return {"Sucesso": "Sucesso"}, 400


@managerRobots_blueprint.route('/manager/stop', methods=['GET'])
def Stop():
    nickName = json.loads(request.data)['nickName']
    if (not (manager is None)) and manager.removeObserver(nickName):
        return {"Sucesso": "Sucesso"}, 200
    return {"Error": "Error"}, 400


@managerRobots_blueprint.route('/manager/positions', methods=['GET'])
def Positions():
    nickName = json.loads(request.data)['nickName']
    symbol = json.loads(request.data)['symbol']
    returnJson = {'profit': getProfitRobot(symbol, nickName)}
    return returnJson, 200
