from app.robots.CrossAverage import CrossAverage
from app.robots.IFR2 import IFR2
from datetime import datetime

symbols = ['BTCUSDT', 'ETHUSDT', 'XRPUSDT']

timeframes = ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
modes = ['Apenas Comprado', 'Apenas Vendido', 'Comprado e Vendido']


def createRobotFromJson(data):
    validateRobot
    data['intervalBegin'] = datetime.strptime(data['intervalBegin'], '%Y-%m-%d %H:%M').time()
    data['intervalEnd'] = datetime.strptime(data['intervalEnd'], '%Y-%m-%d %H:%M').time()

    if (data['type'] == 'IFR2') and validateIFR2(data):
        return IFR2(data['nickName'], data['symbol'], data['timeframe'], data['lot'], data['mode'],
                    data['intervalBegin'], data['intervalEnd'], data['params']['period'], data['params']['upper'],
                    data['params']['lower'], 5)
    elif (data['type'] == 'Cross Average') and validateCrossAverage(data):
        return CrossAverage(data['nickName'], data['symbol'], data['timeframe'], data['lot'], data['mode'],
                            data['intervalBegin'], data['intervalEnd'], data['params']['periodFast'],
                            data['params']['periodSlow'])
    return False


def validateRobot(data):
    if data['nickName'] == '':
        return False
    if data['symbol'] not in symbols:
        return False
    if data['timeframe'] not in timeframes:
        return False
    if data['lot'] <= 0:
        return False
    if data['mode'] not in modes:
        return False
    if data['intervalBegin'] > data['intervalEnd']:
        return False
    return True


def validateIFR2(data):
    if not validateRobot(data):
        return False
    if (data['params']['period'] < 0) or (data['params']['period'] > 100):
        return False
    if (data['params']['upper'] < 0) or (data['params']['upper'] > 100):
        return False
    if (data['params']['lower'] < 0) or (data['params']['lower'] > 100):
        return False
    return True


def validateCrossAverage(data):
    if not validateRobot(data):
        return False
    if (data['params']['periodFast'] < 2) or (data['params']['periodFast'] > 100):
        return False
    if (data['params']['periodSlow'] < 2) or (data['params']['periodSlow'] > 100):
        return False
    return True