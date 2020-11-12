"""
POO - Método super().


"""


class Animal:
    """Classe animal genérica."""

    def __init__(self, nome: str, especie: str) -> None:
        """Construtor."""
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"A {self.__nome} fala {som}.")


class Gato(Animal):
    """Classe que herda de animal."""

    def __init__(self, nome: str, especie: str, raca: str) -> None:
        """Construtor."""
        #Animal.__init__(self, nome, especie)
        super().__init__(nome, especie)
        self.__raca = raca


if __name__ == "__main__":
    an1 = Gato('Atena', 'Felino', 'Angorá')
    an1.faz_som('miau')