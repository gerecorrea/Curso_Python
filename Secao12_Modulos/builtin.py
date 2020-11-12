"""
Trabalhando com módulos built-in.
São módulos integrados, então já vem instalados no Python.

dir(__builtins__)
Dá para verificar todos e melhor explicados na internet
    Como no site python.org, em sua documentação

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
print(rdm.random())  # Agora só reconhece assim.

# Podemos importar todas as funções de um módulo usando *:
    from random import *
    Assim posso utilizar diretamente shuffle(), por ex.

# Nomeando apelidos para as funções específicas tbm:
from random import randint as rdi, random as rdm

Quando se importa diversas funções/classes/etc de um mesmo módulo, costuma-se:
    from random import (
        random,
        randint,
        shuffle,
        choice
    )

"""

from math import pi
print(pi)

def pi():
    return pi
