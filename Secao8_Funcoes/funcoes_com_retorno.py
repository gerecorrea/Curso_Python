"""

Funções com retorno.

Toda função permite retornar valores para quem o chama
    Variável reservada de nome "return"

Caso não retorne, o retorno é do tipo None

Caso contrário, você atribui a variável e utiliza esse retorno
    Pode ser uma ou mais variáveis, uma lista, objetos, classes, etc

Podemos ter diferentes returns dentro de uma mesma função
    Ao executar um "return", sai da função e volta a quem chamou a função
    Sempre somente executará, no máximo, somente um dos return

Abaixo, no código, farei diversas funções exemplo para ter uma ideia
    Algumas não foram realizadas na aula.

OBS EXTRA DA SEÇÃO 11 - EXCEÇÕES:
# Botei para lembrar e auxiliar sobre certos contextos de tipos de retorno
# Para retorno de dicionário na função, assim como tipo None como Optional
from typing import Dict, Optional, Union

def pega_valor(dicionario: str, chave: str) -> Optional[Union[str, Dict[str, str]]]:
    '''Função que pega o valor. O retorno é um dict de chave str e valor str'''
    # Além disso, como pode retornar o tipo None, então deve ter um Option
    # Optional porque é opcional então retornar o dicionário
    # além disso, pode retornar tipo string, então dentro do optional é precis
    # deixar claro que pode retornar ou str ou um dicionário    
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return print('TypeError')

"""

# Import para uso do random()
from random import random


def quadrado_de_7():
    """Docstring."""
    return 7**2


def numeros_naturais_100():
    """Docstring."""
    naturais = list(range(100))
    return naturais


def diz_oi():
    """Docstring."""
    return 'Oi!!!'


def aaa():
    """Docstring."""
    variavel = False
    if variavel is True:
        return "True!"
    elif variavel is not True:
        return "False!"


def retorna_varios():
    """Docstring."""
    return 1, 2, 3, 4


def joga_moeda():
    """Docstring."""
    # Gera um número randomico entre 0 e 1
    valor = random()
    if valor >= 0.5:
        return 'Cara'
    return 'Coroa'
    # Repare que nesse caso não preciso do else


if __name__ == "__main__":
    retorno = quadrado_de_7()
    print(retorno)

    print(numeros_naturais_100())
    # Repare que posso utilizar direto por parametro
    # Sem variável de retorno necessariamente

    print(diz_oi())

    print(aaa())

    num1, num2, num3, num4 = retorna_varios()
    print(num1, num2, num3, num4)

    print(joga_moeda())
