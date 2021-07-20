from flask import Blueprint, request
from app.services.RobotService import *

robots_blueprint = Blueprint('robots_blueprint', __name__)


@robots_blueprint.route('/robots', methods=['GET'])
def getRobots():
    return findAll(request.json)


@robots_blueprint.route('/robot', methods=['GET'])
def getRobot():
    return findOne(request.json)


@robots_blueprint.route('/robots', methods=['POST'])
def createRobot():
    return save(request.json)


@robots_blueprint.route('/robots', methods=['PUT'])
def updateRobot():
    return update(request.json)


@robots_blueprint.route('/robots', methods=['DELETE'])
def deleteRobot():
    return delete(request.json)
