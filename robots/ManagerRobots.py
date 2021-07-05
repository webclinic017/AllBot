from threading import Thread
from roteamento.ConnectionMT5 import connect
from robots.IFR2 import IFR2
import MetaTrader5 as mt5
import pandas as pd
import time

timeframes = {'M1': mt5.TIMEFRAME_M1, 'M2': mt5.TIMEFRAME_M2, 'M5': mt5.TIMEFRAME_M5, 'M15': mt5.TIMEFRAME_M15,
              'M30': mt5.TIMEFRAME_M30, 'H1': mt5.TIMEFRAME_H1, 'H4': mt5.TIMEFRAME_H4, 'D1': mt5.TIMEFRAME_D1}


class DataManager(Thread):
    """Thread responsável por notificar os objetos observadores com os novos dados"""

    def __init__(self, path, login, password):
        Thread.__init__(self)
        self.observers = {}
        self.path = path
        self.login = login
        self.password = password

    def run(self):
        """Inicia a thread"""
        print(connect(path=self.path, login=self.login, password=self.password))
        while True:
            for comb in self.observers:
                symbol, timeframe = comb.split('/')
                rates = mt5.copy_rates_from_pos(symbol, timeframes[timeframe], 0, 100)
                data = pd.DataFrame(rates)
                self.notifyObservers(self.observers[comb], data)
            time.sleep(1)

    def notifyObservers(self, listObservers, data):
        """Notifica os obsevadores com os novos dados"""
        for observer in listObservers:
            observer.newData(data)

    def addObserver(self, robot):
        """Adiciona um observador na lista correspondente a combinação (timeframe + ativo)"""
        comb = robot.comb
        if comb in self.observers:
            self.observers[comb].append(robot)
        else:
            self.observers[comb] = [robot]

    def removeObserver(self, nickName):
        """Remove um observador da lista"""
        for comb in self.observers:
            print(comb)
            for robot in self.observers[comb]:
                if robot.nickName == nickName:
                    robot.closeAll()
                    self.observers[comb].remove(robot)
                return True
        return False
