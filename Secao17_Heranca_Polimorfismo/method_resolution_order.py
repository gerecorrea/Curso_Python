"""
MROPOO -  - Method resolution order.

Herdando o código da aula de herança múltipla, para reaaproveitar o código e
ver melhor sobre o MRO ocorrido naquela aula.

Em Python podemos conferir a ordem de exec dos métodos (MRO) de 3 formas:
    via propriedade da classe __mro__
    via método mro()
    via help

OBS Diego sobre acessos de atributos nas classes filhas:
O acesso aos aitrbutos da classe pai por pate das classes filhas para evitar os
erros do PyLance (por questão de boa escrita de código), devem ser declarados
como protected, ou seja, com apenas um underline (_)

Quanto possuo somente uma classe normal, sem filhos herdados delas, tudo bem
declarar as variáveis privadas (__), porém quando possuo classes filhas e essas
precisarão acessar tais atributos, o correto é criar como protected (_)

Nesta aula uso isso para os atributos.

"""
# from mro import Pinguim  # Output seria Eu sou Tux, da terra
# Então botar na saída Pinguim.__mro__
# Mas o melhor jeito é fazer um help(Pinguim) no console ou main


class Animal:

    def __init__(self, nome: str):
        self._nome = nome

    def cumprimentar(self):
        return f"Eu sou {self._nome}"


class Aquatico(Animal):
    
    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def nadar(self):
        return f"{self._nome} está nadando."

    def cumprimentar(self):
        return f"{self._nome} diz olá, vindo da água."


class Terrestre(Animal):

    def __init__(self, nome: str):
        super().__init__(nome)

    def andar(self):
        return "Ele está andando."

    def cumprimentar(self):
        return f"Eu sou {self._nome}, da terra."


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
    help(Pinguim)  # 'q' para sair.

