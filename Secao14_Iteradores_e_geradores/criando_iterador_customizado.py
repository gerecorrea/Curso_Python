"""
Escrevendo um iterador customizado.

Obs:para isso, precisa-se usar alguns conceitos não aprendidos ainda (no curso)
    Por ex, O.O.

"""


# Criando um por "de baixo dos panos"
class Contador:
    """Classe de iterator iter()."""

    def __init__(self, menor: int, maior: int):
        """Construtor."""
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        """Retorna o objeto em si."""
        return self

    def __next__(self):
        """Todo next lançado, incremento em um, enqto menor que o maior."""
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration  # Quando chegar no fim vai dar um raise stop iter.


con = Contador(1, 61)

print(con.menor)

it = iter(con)

for i in range(con.menor, con.maior):
    print(next(it))
