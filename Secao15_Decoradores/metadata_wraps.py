"""Preservando metadata com wraps.

Metadata (meta-dados) ->  são dados intrísecos em arquivos
    Como a largura, altura, data de modificação, 

Wraps -> São funções que envolvem elementos com diversas finalidades


"""

# Problema:

from typing import Callable
from functools import wraps

def see_login(function: Callable[[], int]) -> str:
    @wraps(function)
    def login(*args, **kwargs) -> str:
        """Eu sou uma função dentro de outra"""
        print(f"Você está chamando {function.__name__}")
        print(f"Aqui a documentação {function.__doc__}")
        return function(*args, **kwargs)
    return login

@see_login
def soma(a: int, b: int) -> int:
    """Soma dois números."""
    return a + b


print(soma.__name__)
print(soma.__doc__)
print(soma(4, 5))