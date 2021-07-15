from mongoengine import *
from datetime import datetime

timeframes = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
symbols = ['BTCUSDT', 'LTCUSDT', 'XRPUSDT']


class RobotSchema(Document):
    apikey = StringField(max_length=50, require=True)
    secret = StringField(max_length=50, require=True)
    owner = ObjectIdField(required=True)
    symbol = StringField(max_length=10, require=True, choices=symbols)
    timeframe = StringField(max_length=10, require=True, choices=timeframes)
    lot = FloatField(min_value=0.00000001, default=0.00000001)
    intervalBegin = DateTimeField(default=datetime(2021, 12, 12, 0, 0, 0))
    intervalEnd = DateTimeField(default=datetime(2021, 12, 12, 23, 59, 59))
    meta = {'collection': 'robots', 'allow_inheritance': True}


class IFR2(RobotSchema):
    periodIFR = IntField(min_value=2, max_value=100, default=2)
    upper = FloatField(min_value=2, max_value=100, default=90)
    lower = FloatField(min_value=2, max_value=100, default=10)
    periodMean = IntField(min_value=2, max_value=200, default=5)


class CrossAverage(RobotSchema):
    periodFast = IntField(min_value=2, max_value=200, default=12)
    periodSlow = IntField(min_value=2, max_value=200, default=24)
