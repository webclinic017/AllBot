from mongoengine import Document, EmbeddedDocument, ListField, DateTimeField, FloatField, IntField, BooleanField, StringField, EmbeddedDocumentListField, ObjectIdField
from datetime import datetime
from src.utils.RobotDataTypes import *

class BackTestSchema(Document):
    stats = ListField(default=[])
    date = DateTimeField(unique=True)
    meta = {'collection': 'backtest'}

class PositionSchema(EmbeddedDocument):
    entryOrderId = IntField(required=True)
    entryQuantity = FloatField(required=True)
    entryCummulativeQuoteQty = FloatField(required=True)
    closeOrderId = IntField()
    closeQuantity = FloatField()
    closeCummulativeQuoteQty = FloatField()
    profit = FloatField()
    open = BooleanField(default=False)
    side = StringField(require=True)

class RobotSchema(Document):
    owner = ObjectIdField(required=True)
    apiKey = StringField(require=True)
    secret = StringField(require=True)
    nickName = StringField(max_length=50, default="Robô")
    symbol = StringField(max_length=10, require=True, choices=symbols)
    timeframe = StringField(max_length=2, require=True, choices=timeframes)
    quantity = FloatField(required=True)
    useInterval = BooleanField(default=False)
    intervalBegin = DateTimeField(default=datetime(2021, 12, 12, 0, 0, 0))
    intervalEnd = DateTimeField(default=datetime(2021, 12, 12, 23, 59, 59))
    started = BooleanField(default=False)
    positions = EmbeddedDocumentListField(PositionSchema)
    meta = {'collection': 'robots', 'allow_inheritance': True}

class IFR2Schema(RobotSchema):
    periodIFR = IntField(min_value=2, max_value=100, default=2)
    upper = FloatField(min_value=2, max_value=100, default=90)
    lower = FloatField(min_value=2, max_value=100, default=10)
    periodMean = IntField(min_value=2, max_value=200, default=5)

class CrossAverageSchema(RobotSchema):
    periodFast = IntField(min_value=2, max_value=200, default=12)
    periodSlow = IntField(min_value=2, max_value=200, default=24)






