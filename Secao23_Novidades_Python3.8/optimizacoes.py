"""

Melhorias:
    Tempo de procura de um objeto
    Otimização da alocação de memória (usando menos bytes)
    São melhorias pequenas, de forma geral.

"""

import collections
from timeit import timeit

# Forma rápida de criar classe
Pessoa = collections.namedtuple('Pessoa', 'nome email')

felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')

# exemplo de teste, teria que comparar com o py3.7, por ex, para ver a dif
print(timeit('felicity.email', globals=globals()))

# OBS: o globals retorna o contexto geral, dunders gerais
print(globals())


import sys
print(sys.getsizeof(list(range(1000))))
