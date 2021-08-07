from mongoengine import *
from datetime import datetime
from RobotDataTypes import *


class RankingSchema(Document):
    stats = ListField(default=[])
    meta = {'collection': 'ranking'}


class BackTestSchema(Document):
    stats = DictField(required=True)
    comb = DictField()
    meta = {'collection': 'backtest'}


class PositionSchema(EmbeddedDocument):
    entryOrderId = IntField(required=True)
    entryQuantity = FloatField(required=True)
    entryCummulativeQuoteQty = FloatField(required=True)
    closeOrderId = IntField()
    closeQuantity = FloatField()
    closeCummulativeQuoteQty = FloatField()
    profit = FloatField()
    openResult = FloatField()
    open = BooleanField(default=False)
    side = StringField(require=True)
    lastUpdate = DateTimeField(default=datetime(2021, 12, 12, 0, 0, 0))


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
    mode = StringField(choices=modes, default='onlybuy')
    status = StringField(choices=status, default='inactive')
    positions = EmbeddedDocumentListField(PositionSchema)
    meta = {'collection': 'robots', 'allow_inheritance': True}


class IFR2Schema(RobotSchema):
    periodIFR = IntField(min_value=2, max_value=100, default=2)
    upper = FloatField(min_value=2, max_value=100, default=90)
    lower = FloatField(min_value=2, max_value=100, default=10)
    periodMean = IntField(min_value=2, max_value=200, default=5)

    def comb(self):
        return {"type": "IFR2",
                "symbol": self.symbol,
                "timeframe": self.timeframe,
                "periodIFR": self.periodIFR,
                "periodMean": self.periodMean,
                "lower": self.lower,
                "upper": self.upper}


class CrossAverageSchema(RobotSchema):
    periodFast = IntField(min_value=2, max_value=200, default=12)
    periodSlow = IntField(min_value=2, max_value=200, default=24)

    def comb(self):
        return {"type": "CROSSAVERAGE",
                "symbol": self.symbol,
                "timeframe": self.timeframe,
                "periodFast": self.periodFast}