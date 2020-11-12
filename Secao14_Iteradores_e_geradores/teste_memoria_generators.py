"""
Teste de memória com Generators.


"""

from typing import List


def fib_lista(max: int) -> List[int]:
    """Retorna a sequencia de fibonacci."""
    nums = []
    a, b = 0, 1
    while (len(nums)) < max:  # Eqnt quantidade de elem. em nums < max
        nums.append(b)  # Insere o elemento b na lista nums
        a, b = b, a + b  # a recebe b, e b recebe a + b
    return nums


# Teste 1 - usou 489MB de consumo de RAM durante todo o proceso:
for n in fib_lista(10):
    print(n)


# Função usando geradores agora:

def fib_gen(max: int):
    """Retorna a sequencia de fibonacci usando geradores, retorna yield."""
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# Teste 2 - geradores - 2,8MB de consumo de RAM durante todo o processo:
for n in fib_gen(10):
    print(n)
# OBS: Na minha máquina foi 0,3% de 4GB RAM e 77% de CPU, aprox
