from unittest import TestCase, main
from roteamento.OrderSend import *
from roteamento.ConnectionMT5 import connect

class TestOrderSend(TestCase):

    def test_case01(self):
        """Caso de Teste onde o são passados parâmetros válidos para o envio da compra"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9", server="ICMarkets-Demo")
        esperado = True
        resultado = buyMarket("GBPUSD", 0.01, 1000, 1000, 2424, "test_case01")
        self.assertEqual(esperado, resultado)

    def test_case02(self):
        """Caso de Teste onde o são passados parâmetros válidos para o envio da venda"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9", server="ICMarkets-Demo")
        esperado = True
        resultado = sellMarket("GBPUSD", 0.01, 1000, 1000, 2424, "test_case02")
        self.assertEqual(esperado, resultado)

    def test_case03(self):
        """Caso de Teste onde é passado um ativo inválido para o envio da compra"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9", server="ICMarkets-Demo")
        esperado = "Ativo Inválido"
        resultado = buyMarket("Groselha", 0.01, 1000, 1000, 2424, "test_case03")
        self.assertEqual(esperado, resultado)

    def test_case04(self):
        """Caso de Teste onde é passado um ativo inválido para o envio da venda"""

        connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9", server="ICMarkets-Demo")
        esperado = "Ativo Inválido"
        resultado = sellMarket("Groselha", 0.01, 1000, 1000, 2424, "test_case04")
        self.assertEqual(esperado, resultado)

if __name__ == '__main__':
    main()