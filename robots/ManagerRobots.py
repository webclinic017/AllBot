from threading import Thread
import websocket
import json
from robots.IFR2 import IFR2

SOCKET = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_1m"


class DataManager(Thread):
    """Thread responsável por notificar os objetos observadores com os novos dados"""

    def __init__(self):
        Thread.__init__(self)
        self.observers = {}
        self.dataframes = {}

    def on_open(self, ws):
        print('opened connection')

    def on_close(self, ws):
        print('closed connection')

    def on_message(self, ws, message):
        data = json.loads(message)
        if data['data']['k']['x'] or True:
            comb = data['data']['k']['s'] + '/' + data['data']['k']['i']
            self.calcIndicators(comb)
            self.notifyObservers(comb, data)

    def run(self):
        """Inicia a thread"""
        ws = websocket.WebSocketApp(SOCKET, on_open=self.on_open, on_close=self.on_close, on_message=self.on_message)
        ws.run_forever()

    def notifyObservers(self, comb, data):
        """Notifica os obsevadores com os novos dados"""
        for observer in self.observers[comb]:
            observer.newData(data)

    def addObserver(self, robot):
        """Adiciona um observador na lista correspondente a combinação (ativo + timeframe)"""
        comb = robot.comb
        if comb in self.observers:
            self.observers[comb].append(robot)
        else:
            self.observers[comb] = [robot]

    def removeObserver(self, nickName):
        """Remove um observador da lista"""
        for comb in self.observers:
            for robot in self.observers[comb]:
                if robot.nickName == nickName:
                    robot.closeAll()
                    self.observers[comb].remove(robot)
                return True
        return False


ifr = IFR2("IFR2-1", "BTCUSDT", "1m", 2, 10, 90, 43, 3434, 122, 1212, 1212)
a = DataManager()
a.addObserver(ifr)
a.start()
