from .Schemas import RobotSchema
from bson import ObjectId
import json


def save(data):
    robot = RobotSchema.from_json(data).save()
    return json.loads(robot.to_json())


def update(data):
    values = data.copy()
    values.pop('_id')
    return json.loads(RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).update(**values))


def delete(data):
    RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).delete()
    return {"SUCESS": "sucesso"}


def findAll(data):
    return json.loads(RobotSchema.objects(owner=ObjectId(data['_id']["$oid"]).to_json()))


def findOne(data):
    return json.loads(RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).to_json())
