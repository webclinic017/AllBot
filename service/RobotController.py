from database.RobotDAO import *
from flask import Blueprint, request, session
import json

robots_blueprint = Blueprint('robots_blueprint', __name__)


@robots_blueprint.route('/robots', methods=['GET'])
def getRobots():
    data = {'email': session['userAccount']['email']}
    return {"robots": findAll(data)}, 200


@robots_blueprint.route('/robots', methods=['POST'])
def createRobot():
    return save(request.data), 201


@robots_blueprint.route('/robots', methods=['PUT'])
def updateRobot():
    data = json.loads(request.data)
    return {"robot": update(data)}, 200


@robots_blueprint.route('/robots', methods=['DELETE'])
def deleteRobot():
    data = json.loads(request.data)
    return delete(data), 200
