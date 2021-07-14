from ..database.RobotSchema import RobotSchema
from flask import Blueprint, request
from bson.objectid import ObjectId

robots_blueprint = Blueprint('robots_blueprint', __name__)


@robots_blueprint.route('/robots', methods=['GET'])
def getRobots():
    result = RobotSchema.objects(owner=ObjectId(request.data['_id']["$oid"]))
    print(result)
    return result, 200


# @robots_blueprint.route('/robots', methods=['POST'])
# def createRobot():
#     return save(request.data), 201
#
#
# @robots_blueprint.route('/robots', methods=['PUT'])
# def updateRobot():
#     data = json.loads(request.data)
#     return {"robot": update(data)}, 200
#
#
# @robots_blueprint.route('/robots', methods=['DELETE'])
# def deleteRobot():
#     data = json.loads(request.data)
#     return delete(data), 200
