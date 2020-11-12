"""Geradores.

- Generators (geradores) são Iterators (iteradores)
    Mas o contrário não é válido, pois nem todo Iterator é um Generator

Outras info:
    Generators podem ser criados com um funções geradoras
    Funções geradores utilizam a palavra reserva yield
    Generators podem ser criados com expressões geradoras

    Diferenças entre funções e generator function (funções geradoras):

    Funções                 |        Generator Function
    ---------------------------------------------------
    Utilizam return         |     Utilizam yield
    Retorna uma vez         |     Podem utilizar o yield múltiplas vezes
    Qndo exec,retorna valor |    Qndo exec, retorna um generator

"""

from typing import Iterator


# Exemplo de generator function:
def conta_ate(valor_max: int) -> Iterator[int]:
    """Função generator, não sairá dela enquanto não finalizar tudo dela."""
    contador = 1
    while contador <= valor_max:
        yield contador  # retorna o valor, mas fica esperando dentro da função
        # No caso do return sairia da função
        contador = contador + 1

gen = conta_ate(10)

for _ in range(1, 10):
    print(next(gen))  # Mesmo que print(iterado do for, como um "i")

for num in gen:
    print(num)