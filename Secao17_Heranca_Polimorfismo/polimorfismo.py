"""
Polimorfismo.

Referente as várias formas dos métodos em seus métodos conforme seus contextos

Quandoa  gente reimplementa um método presente na classe pai em classes filhas
estamos realizando uma sobreescrita de método (OVerriding)
    Ela é a melhor representação do polimorfismo

"""


class Animal(object):
    def __init__(self, nome: str) -> None:
        self._nome = nome  # protected

    def falar(self) -> None:
        raise NotImplementedError('A classe filha implementa tal método.')

    def comer(self) -> None:
        print(f"{self._nome} está comendo.")


class Cachorro(Animal):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def falar(self) -> None:
        print(f"{self._nome} fala au au.")


class Rato(Animal):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)


if __name__ == "__main__":
    felix = Cachorro('Felix')
    felix.falar()
    
    quinn = Rato('Quinn')
    quinn.falar()  # Neste vai retornar o raise declarado, pois o método
    # não foi declarado na classe Rato