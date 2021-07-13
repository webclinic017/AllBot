from mongoengine import *
from datetime import datetime


class RobotSchema(Document):
    apikey = StringField(max_length=50, require=True)
    secret = StringField(max_length=50, require=True)
    nickName = StringField(max_length=50, require=True)
    symbol = StringField(max_length=50, default="GBPUSD")
    timeframe = StringField(max_length=50, default="M1")
    lot = FloatField(max_length=50, default=0.01)
    magicNumber = IntField(max_length=50, default=2424)
    intervalBegin = DateTimeField(default=datetime(2021, 12, 12, 0, 0, 0))
    intervalEnd = DateTimeField(default=datetime(2021, 12, 12, 23, 59, 59))
    mode = StringField(max_length=50, default="Comprado e Vendido")
    params = DictField(default={})
    meta = {'collection': 'robots'}
