

class Robo:

    def __init__(self, nome: str, bateria: int = 100):
        """Construtor. Usando variáveis com protected."""
        self._nome = nome
        self._bateria = bateria
        self._habilidade = []  # lista de habilidades vazia inicialmente

    @property
    def nome(self):
        return self._nome

    @property
    def bateria(self):
        return self._bateria

    @property
    def habilidades(self):
        return self._habilidade

    def carregar(self):
        self._bateria = 100

    def dizer_nome(self):
        if self._bateria > 0:
            self._bateria -= 2
            return f'beep boop. Eu sou {self._nome.upper()}.'
        return 'Bateria zerada, por favor recarregue.'

    def aprender_habilidade(self, nova_habilidade: str, custo: int):
        if self._bateria >= custo:
            self._bateria -= custo
            self._habilidade.append(nova_habilidade)
            return f'Uow, aprendi a {nova_habilidade}.'
        return 'Bateria insuficiente. Recarregue e tente novamente.'