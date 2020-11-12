import unittest

from robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        """Como ele executa antes, podemos criar o objeto e ter acesso mais
        facilmente aos objetos nas funções seguintes."""
        self.megaman = Robo('Mega man', bateria=50)
        print('Set up sendo executado!')
    
    def test_carregar(self):
        # megaman = Robo('Mega man', bateria=50)  # sem declaração no setUp()
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        # megaman = Robo('Mega man', bateria=50)
        self.assertEqual(self.megaman.dizer_nome(), 'beep boop. Eu sou MEGA MAN.')
        self.assertEqual(self.megaman.bateria, 48, 'A bateria deveria estar em 48%')

    def tearDown(self):
        print('O tearDown() foi executado.')

if __name__ == "__main__":
    unittest.main()

