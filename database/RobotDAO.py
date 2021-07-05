from mongoengine import *
from database.RobotSchema import RobotSchema
import json
from flask import session
from bson import ObjectId

connection = connect(db='Allbot_Backend',
                     host='mongodb+srv://AllBot:123qwe@cluster0.7lypu.mongodb.net/Allbot_Backend?retryWrites=true&w=majority')


def save(data):
    a = RobotSchema().from_json(data)
    a.email = session['userAccount']['email']
    a.save()
    return json.loads(a.save().to_json())


def update(data):
    values = data.copy()
    values.pop('_id')
    print(data)
    return RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).update(**values)


def delete(data):
    RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).delete()
    return {"SUCESS": "sucesso"}


def findAll(data):
    return json.loads(RobotSchema.objects(email=data['email']).to_json())


def findOne(data):
    return json.loads(RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).to_json())
