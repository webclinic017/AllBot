from src.robots.IFR2 import IFR2
from src.robots.CrossAverage import CrossAverage
from src.robots.BollingerBands import BollingerBands
from src.robots.BollingerBandsML import BollingerBandsML
from src.database.Schemas import IFR2Schema, CrossAverageSchema, BollingerBandsSchema, BollingerBandsSchemaML


def IFR2FromSchema(robotSchema):
    inPosition = robotSchema.positions and robotSchema.positions[-1].open
    robot = IFR2(str(robotSchema.id),
                 robotSchema.apiKey,
                 robotSchema.secret,
                 robotSchema.nickName,
                 robotSchema.symbol,
                 robotSchema.timeframe,
                 robotSchema.quantity,
                 robotSchema.intervalBegin,
                 robotSchema.intervalEnd,
                 inPosition,
                 robotSchema.chatID,
                 robotSchema.onlyNotify,
                 robotSchema.periodIFR,
                 robotSchema.upper,
                 robotSchema.lower,
                 robotSchema.periodMean)

    return robot


def CrossAverageFromSchema(robotSchema):
    inPosition = robotSchema.positions and robotSchema.positions[-1].open
    robot = CrossAverage(str(robotSchema.id),
                         robotSchema.apiKey,
                         robotSchema.secret,
                         robotSchema.nickName,
                         robotSchema.symbol,
                         robotSchema.timeframe,
                         robotSchema.quantity,
                         robotSchema.intervalBegin,
                         robotSchema.intervalEnd,
                         inPosition,
                         robotSchema.chatID,
                         robotSchema.onlyNotify,
                         robotSchema.periodFast,
                         robotSchema.periodSlow)

    return robot


def BollingerBandsFromSchema(robotSchema):
    inPosition = robotSchema.positions and robotSchema.positions[-1].open
    robot = BollingerBands(str(robotSchema.id),
                           robotSchema.apiKey,
                           robotSchema.secret,
                           robotSchema.nickName,
                           robotSchema.symbol,
                           robotSchema.timeframe,
                           robotSchema.quantity,
                           robotSchema.intervalBegin,
                           robotSchema.intervalEnd,
                           inPosition,
                           robotSchema.chatID,
                           robotSchema.onlyNotify,
                           robotSchema.period,
                           robotSchema.stdDeviation)
    return robot


def BollingerBandsFromSchemaML(robotSchema):
    inPosition = robotSchema.positions and robotSchema.positions[-1].open
    robot = BollingerBandsML(str(robotSchema.id),
                             robotSchema.apiKey,
                             robotSchema.secret,
                             robotSchema.nickName,
                             robotSchema.symbol,
                             robotSchema.timeframe,
                             robotSchema.quantity,
                             robotSchema.intervalBegin,
                             robotSchema.intervalEnd,
                             inPosition,
                             robotSchema.chatID,
                             robotSchema.onlyNotify,
                             robotSchema.period,
                             robotSchema.stdDeviation)
    return robot


def getRobotFromSchema(robotSchema):
    if isinstance(robotSchema, IFR2Schema):
        return IFR2FromSchema(robotSchema)
    if isinstance(robotSchema, CrossAverageSchema):
        return CrossAverageFromSchema(robotSchema)
    if isinstance(robotSchema, BollingerBandsSchema):
        return BollingerBandsFromSchema(robotSchema)
    if isinstance(robotSchema, BollingerBandsSchemaML):
        return BollingerBandsFromSchemaML(robotSchema)
