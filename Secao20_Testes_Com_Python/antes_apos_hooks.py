"""

hooks.

São os testes em si, ou seja, a execução dos testes


setup() -> é executado antes de cada método de teste. É util para criarmos
instânca de objetos e outros dados

tearDown() -> é executado ao final de cada método de teste. É útil para exlcuir
dados ou fechar conexões com banco de dados.

"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        #Config do setUp()
        pass

    def test_primeiro(self):
        # set
        pass

    def tearDown(self):
        # config do tearDown()
        pass