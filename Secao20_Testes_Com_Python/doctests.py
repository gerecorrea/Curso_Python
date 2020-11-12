"""
Docstests.

São testes que colocamos na docstring do python.

# para executar o teste, não se faz padrão python doctests.py, mas sim:
$ python -m doctest -v doctests.py

O retorno testado e esperado deve estar entre comentário do tipo aspas duplas
triplas
E deve ser rodado com o formato definido acima.
Ele irá retorna a quantidade de testes e item sucedidos e falhos.

O próprio professor tbm não curte o doctests, dado que você precisar dar 
o comportamento esperado. Também não achei mto bom não.

"""


from typing import List


def soma(a: int, b: int) -> int:
    """ soma entre numeros a e b
    >>> soma(1, 2)
    3
    """

    return a + b    
    

# Outro xemplo, aplicando o TDD:

def duplicar(valores) -> List[int]:
    # for i in valores:
        # valores[i] *= 2

    """ dupla os valores de uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar([True, None])
    Traceback (most recent call last)
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elemento for elemento in valores]
