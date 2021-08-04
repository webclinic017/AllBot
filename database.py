from mongoengine import *

connection = connect(db='Bots',
                     host="mongodb+srv://dev:groselha24@allbot.poydz.mongodb.net/Bots?retryWrites=true&w=majority")


class BackTestSchema(Document):
    stats = ListField(default=[])
    date = DateTimeField(unique=True)
    meta = {'collection': 'backtest'}
