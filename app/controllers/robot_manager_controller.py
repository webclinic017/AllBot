from app.services.RobotManagerService import *
from flask import request, Blueprint


managerRobots_blueprint = Blueprint('managerRobots_blueprint', __name__)


@managerRobots_blueprint.route('/manager/start', methods=['PUT'])
def Play():
    return startRobot(request.json)


@managerRobots_blueprint.route('/manager/stop', methods=['PUT'])
def Stop():
    return stopRobot(request.json)


