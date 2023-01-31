from app.database.Schemas import *
from app.utils.Message import *
from app.database.Parsers import *
from flask import jsonify
from bson import ObjectId
import json


def save(data):
    try:
        if data['type'] == 'IFR2':
            data.pop("type")
            return jsonify(robotDTO(json.loads(IFR2Schema.from_json(json.dumps(data)).save().to_json()))), 201
        elif data['type'] == 'CROSSAVERAGE':
            data.pop("type")
            return jsonify([robotDTO(robot) for robot in json.loads(CrossAverageSchema.from_json(json.dumps(data)).save().to_json())]), 201
    except:
        return ERROR_UNCREATED_ROBOT, 400


def update(data):
    try:
        values = data.copy()
        values.pop('id')
        robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
        if robot and (str(robot.owner) == data['owner']) and robot.update(**values):
            return SUCCESS_UPDATE, 200
        return ERROR_NOT_UPDATED_ROBOT, 400
    except:
        return ERROR_NOT_UPDATED_ROBOT, 400


def delete(data):
    try:
        robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
        if robot and (str(robot.owner) == data['owner']):
            robot.delete()
            return SUCCESS_REMOVE, 200
        return ERROR_UNDELETED_ROBOT, 400
    except:
        return ERROR_UNDELETED_ROBOT, 400


def findAll(data):
    try:
        return jsonify([robotDTO(robot) for robot in json.loads(RobotSchema.objects(owner=ObjectId(data['owner'])).to_json())]), 200
    except:
        return RESOURCE_NOT_FOUND, 400


def findOne(data):
    try:
        robot = RobotSchema.objects(id=ObjectId(data['id'])).first()
        if robot and (str(robot.owner) == data['owner']):
            return jsonify(robotDTO(json.loads(robot.to_json()))), 200
        return RESOURCE_NOT_FOUND, 400
    except:
        return RESOURCE_NOT_FOUND, 400



