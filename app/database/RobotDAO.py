# from database.Connection import mongo
# from database.RobotSchema import RobotSchema
# import json
#
#
# def save(data):
#     robot = RobotSchema.from_json(data)
#     return json.loads(a.save().to_json())
#
#
# def update(data):
#     values = data.copy()
#     values.pop('_id')
#     print(data)
#     return RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).update(**values)
#
#
# def delete(data):
#     RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).delete()
#     return {"SUCESS": "sucesso"}
#
#
# def findAll(data):
#     return json.loads(RobotSchema.objects(email=data['email']).to_json())
#
#
# def findOne(data):
#     return json.loads(RobotSchema.objects(id=ObjectId(data['_id']["$oid"])).to_json())
