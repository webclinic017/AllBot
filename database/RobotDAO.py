from flask import Flask, jsonify, request, redirect
from flask_pymongo import PyMongo

from database.RobotSchema import RobotSchema

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://dev:<password>@allbot.poydz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
mongo = PyMongo(app)

app.run(debug=True)

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
