from unittest import TestCase, main
from app.roteamento import connect

class TestPosition(TestCase):

    def test_case01(self):
        """Caso de Teste onde é verfificado se existe posição em aberto, quando existe compra"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9", server="ICMarkets-Demo")
        closePosition("GBPUSD", 2424)
        buyMarket("GBPUSD", 0.01, 1000, 1000, 2424, "test_case01")
        esperado = True
        resultado = hasOpenPosition("GBPUSD")
        self.assertEqual(esperado, resultado)

    def test_case02(self):
        """Caso de Teste onde é verfificado se existe posição em aberto, quando existe venda"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9", server="ICMarkets-Demo")
        closePosition("GBPUSD", 2424)
        sellMarket("GBPUSD", 0.01, 1000, 1000, 2424, "test_case02")
        esperado = True
        resultado = hasOpenPosition("GBPUSD")
        self.assertEqual(esperado, resultado)

    def test_case03(self):
        """Caso de Teste onde é verfificado se existe posição de compra em aberto, quando não existe"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9",
                server="ICMarkets-Demo")
        closePosition("GBPUSD", 2424)
        esperado = False
        resultado = isLongPosition("GBPUSD")
        self.assertEqual(esperado, resultado)

    def test_case04(self):
        """Caso de Teste onde é verfificado se existe posição de venda em aberto, quando não existe"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9",
                server="ICMarkets-Demo")
        closePosition("GBPUSD", 2424)
        esperado = False
        resultado = isShortPosition("GBPUSD")
        self.assertEqual(esperado, resultado)

if __name__ == '__main__':
    main()