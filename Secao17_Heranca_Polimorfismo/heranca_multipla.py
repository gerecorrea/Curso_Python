"""
Continuação de herança.

Herança múltipla: implica vocÊ poder herdar de múltiplas classes
    Em Java e outras linguagens só podemos herdar de uma.
    Podendo aqui, herar diversos atirbutos de diversas superclasses

Pode ser feita de duas maneiras:
    Multiderivação direta: uma classe filha que herda diretamente de n classes
    diferentes que não possuem relação com outras
    Multiderivação indireta: uma classe filha que herda de uma que herda de
    outra, herdando multiplamente indiretamente.

Apesar disso, independe o tipo, a classe que herdar de outra, herdará todos os
atributos e métodos de suas superclasses
"""


# Exemplo de multiderivação direta - herda diretamente classes não relacionadas:
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo de multiderivaçao indireta - herda por efeito cascata:
class Base4:
    pass


class Base5(Base4):
    pass


class Base6(Base5):
    pass


class MultiDerivada2(Base6):
    pass

# Exemplo prático:


class Animal:

    def __init__(self, nome: str):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"


class Aquatico(Animal):
    
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando."

    def cumprimentar(self):
        return f"{self._Animal__nome} diz olá, vindo da água."


class Terrestre(Animal):

    def __init__(self, nome: str):
        super().__init__(nome)

    def andar(self):
        return f"Ele está andando."

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome}, da Terra."


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome: str):
        super().__init__(nome)


if __name__ == "__main__":
    gato = Terrestre('corex')
    print(gato.cumprimentar())  # retorna o sobreescrito de Terrestre
    tux = Pinguim('tux')
    print(tux.andar())
    print(tux.nadar())
    print(tux.cumprimentar())  # Eu sou o tux da terra?? MRO
    # No caso temos duas funções cumprimentar, ele chama a segunda, é um caso de
    # MRO, veremos nas aulas seguintes.

    print(f'Tux é instância de Pinguim: {isinstance(tux, Pinguim)}')
    print(f'Tux é instância de Aquático: {isinstance(tux, Aquatico)}')
    print(f'Tux é instância de Terrestre: {isinstance(tux, Terrestre)}')
    print(f'Tux é instância de Animal: {isinstance(tux, Animal)}')
    print(f'Tux é um objeto: {isinstance(tux, object)}')
    # Sim para todos, pois direta ou indiretamente herda deles todos.
    # o do object pq class é desse tipo
    # oficialmente seria até clase Nome(object): ...