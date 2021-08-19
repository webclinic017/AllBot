from src.marketData.IndicatorsManager import indicators
from binance.websocket.spot.websocket_client import SpotWebsocketClient as Client


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
        """Notificação de novos dados da exchange"""
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

        for comb in self.observers:
            for r in self.observers[comb]:
                if r.id == robot.id:
                    return

        comb = robot.comb
        if comb in self.observers:
            self.observers[comb].append(robot)
        else:
            self.observers[comb] = [robot]
            self.client.instant_subscribe(
                stream=self.getStream(robot.symbol, robot.timeframe),
                callback=self.on_message,
            )
        if not self.client.is_alive():
            self.client.start()

    def removeObserver(self, id):
        """Remove um observador da lista"""
        for comb in self.observers:
            for robot in self.observers[comb]:
                if robot.id == id:
                    self.observers[comb].remove(robot)

    def getStream(self, symbol, timeframe):
        return symbol.lower() + '@kline_' + timeframe.lower()


datamanager = DataManager()



