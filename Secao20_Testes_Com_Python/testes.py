""" Para executar esses testes basta executar python3.8 testes.py no terminal"""
"""Baseado no arquivo atividades.py, que é onde estão os métodos,
todos vão passar"""

import unittest

from atividades import comer, dormir, nome


# Nomeamos geralemtne com mesmo nome do arquivo
class AtividadesTestes(unittest.TestCase):
    """No classe que herda do unittest. TestCase tem vários assertions.
    Existem vários métodos (procurar unittest métodos na internet).
    Alguns são assertEqual(a,b), assertNotEqual(a,b), assertTrue(a,b)
    assertIs(s), etc."""
    """Usa-se test_nomeMétodo por padrão. Caso coloca-se dentro da função
    com a flag -v ele retorna o docstring tbm."""
    
    def test_comer_saudavel(self):
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo por conta da dieta.'
        )

    def test_comer_gostosa(self):
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'fome de commida gostosa.'
        )

    def test_dormir_pouco(self):
        self.assertEqual(
            dormir(4),
            'Continuo cansado, dormi pouco.'
        )
    
    def test_dormir_muito(self):
        self.assertEqual(
            dormir(10),
            'Droga, dormi demais.'
        )

    def test_nome(self):
        self.assertEqual(True, nome('Geremias Correa')), 'Tá certo'
        # Poderia usar o assertTrue e passar só um param, por ex

if __name__ == "__main__":
    unittest.main()
    # vai varrer seu arquivo e executar cada teste do testCase um a um.