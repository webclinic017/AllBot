from unittest import TestCase, main
from roteamento.ConnectionMT5 import connect

class TestConnectMT5(TestCase):

    def test_case01(self):
        """Caso de Teste onde o usuário informa os dados corretos em relação a plataforma de negociação"""

        esperado = True
        resultado = connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=50498337, password="Pkvxcav9", server="ICMarkets-Demo")
        self.assertEqual(esperado, resultado)

    def test_case02(self):
        """Caso de Teste onde o usuário informa uma conta inválida para a plataforma de negociação"""

        esperado = (-6, 'Terminal: Authorization failed')
        resultado = connect(path="C:\Program Files\MetaTrader 5\\terminal64.exe", login=20, password="zVvtfanE", server="ICMarkets-Demo")
        self.assertEqual(esperado, resultado)

    def test_case03(self):
        """Caso de Teste onde o usuário informa um path inválido para a plataforma de negociação"""

        esperado = (-10003, "IPC initialize failed, Process create failed 'patherrado'")
        resultado = connect(path="patherrado", login=50452554, password="zVvtfanE", server="ICMarkets-Demo")
        self.assertEqual(esperado, resultado)

if __name__ == '__main__':
    main()