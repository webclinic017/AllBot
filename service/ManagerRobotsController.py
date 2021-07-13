from robots.ManagerRobots import DataManager
from robots.RobotUtils import createRobotFromJson
from flask import Blueprint, request

import json

managerRobots_blueprint = Blueprint('managerRobots_blueprint', __name__)

manager = None


@managerRobots_blueprint.route('/manager/play', methods=['GET'])
def Play():
    global manager
    robot = createRobotFromJson(json.loads(request.data))
    if robot:
        if manager is None:
            manager = DataManager()
        manager.addObserver(robot)
        if not manager.is_alive():
            manager.start()
        return {"Sucesso": "Sucesso"}, 200
    else:
        return {"Error": "Error"}, 400


@managerRobots_blueprint.route('/manager/stop', methods=['GET'])
def Stop():
    nickName = json.loads(request.data)['nickName']
    if (not (manager is None)) and manager.removeObserver(nickName):
        return {"Sucesso": "Sucesso"}, 200
    return {"Error": "Error"}, 400


@managerRobots_blueprint.route('/manager/positions', methods=['GET'])
def getSummary():
    return {"Sucesso": "Sucesso"}, 200
