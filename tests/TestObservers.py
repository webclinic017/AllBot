from robots.ManagerRobots import DataManager
from robots.CrossAverage import CrossAverage
from robots.IFR2 import IFR2

"""Testando estrutura com o padrão observer nas estratégias"""

ca = CrossAverage("CA-1", "GBPUSD", "H1", 0.01, "Apenas Comprado", intervalBegin, intervalEnd, 10, 20)

ifr = IFR2("IFR2-1", "EURUSD", 1212, 2, 10, 90)


a = DataManager()
a.addObserver(ca)
a.addObserver(ifr)
a.start()
