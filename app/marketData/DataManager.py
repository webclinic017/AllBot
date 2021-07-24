from app.robots.IFR2 import IFR2
from app.marketData.IndicatorsManager import indicators
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client


def getStream(symbol, timeframe):
    return symbol.lower() + '@kline_' + timeframe.lower()


class DataManager:
    """Thread responsável por notificar os objetos observadores com os novos dados"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.observers = {}
        self.dataframes = {}
        self.client = Client()

    def on_message(self, data):
        if data['k']['x'] or True:
            comb = data['k']['s'] + '/' + data['k']['i']
            self.notifyObservers(comb, data)

    def notifyObservers(self, comb, data):
        """Notifica os obsevadores com os novos dados"""
        closed = data['k']['x']
        if closed:
            indicators.newData(comb, data)
        for observer in self.observers[comb]:
            observer.newData(data, closed)

    def addObserver(self, robot):
        """Adiciona um observador na lista correspondente a combinação (ativo + timeframe)"""
        comb = robot.comb
        if comb in self.observers:
            self.observers[comb].append(robot)
        else:
            self.observers[comb] = [robot]
            self.client.instant_subscribe(
                stream=getStream(robot.symbol, robot.timeframe),
                callback=self.on_message,
            )
        if not self.client.is_alive():
            self.client.start()

    def removeObserver(self, nickName):
        """Remove um observador da lista"""
        for comb in self.observers:
            for robot in self.observers[comb]:
                if robot.nickName == nickName:
                    robot.closeAll()
                    self.observers[comb].remove(robot)
                return True
        return False


datamanager = DataManager()

#
# key = "VI6hVdW4xVtr4CXponITFo4217t2Xoxx0xcSfbZUfUupOV1on2GgPPBBYUbLamrn"
# secret = "l2oqsYuxpGfQzSmS9WeEvKRGdjsFEQEgzNCkGIg7x49o8nEOZjOgppcamgGN5qLv"
#
# ifr = IFR2(key, secret, "IFR2-1", "BTCUSDT", "1m", 50, 0, 24, 2, 90, 90, 20)
# #ifr = IFR2("IFR2-1", "BTCUSDT", "1m", 2, 0, 24, 2, 90, 90, 20)
# datamanager.addObserver(ifr)
# #datamanager.addObserver(ifr2)

