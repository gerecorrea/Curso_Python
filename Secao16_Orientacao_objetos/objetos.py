"""
Objetos.

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do
mundo real para sua representação computacional, devemos poder criar quantos
objetos forem necessários. Podemos pensar neles como variáveis do tipo defini-
do de uma classe

"""


class Lampada:
    """Docstring da calsse lâmpada."""

    contador = 0

    def __init__(self, cor: str, voltagem: int, luminosidade: int):
        """Docstring do construtor."""
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False
        self.__id = Lampada.contador
        Lampada.contador = self.__id + 1

    def checa_lampada(self):
        """Checa se a lâmpada está ligada."""
        return self.ligada

    def ligar_desligar(self):
        """Liga Pressiona o interruptor."""
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True


class Interruptor:
    """Classe que possui como membro a classe Lampada, para ex basico."""

    def __init__(self, lampada: Lampada):
        """Construtor."""
        self.lampada = lampada

    def change(self):
        """Muda o estado da lâmpada. Método de outra classe."""
        self.lampada.ligar_desligar()

    def estado_lampada(self):
        """Retorna o estado atual da lampada da outra classe."""
        return self.lampada.checa_lampada()


# Instâncias e operações com os métodos para demonstração:
l1 = Lampada('branca', 220, 60)
print("Estado da lâmpada: ", l1.checa_lampada())
print("Liga/desliga", l1.ligar_desligar())
print("Estado da lâmpada: ", l1.checa_lampada())

# l2 = Lampada()  # Retorna erro pela falta de argumentos
# Então têm-se que da forma atual de declaração, todos parametros são obg.]

# Definindo uma classe que seja variável a qtd de parâmetros:

interr1 = Interruptor(l1)
print(interr1.estado_lampada())
interr1.change()
print(interr1.estado_lampada())

