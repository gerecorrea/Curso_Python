"""
Funções de maior grandeza (Higher Order Functions - HOF).

HOF ->

Quando uma linguagem permite a utilização do HOF, indica que podemos ter
funções que retornam outras funções como resultados ou mesmo que podemos
passar funções como argumentos para outras funções
Além da criação de variáveis do tipo funções nos nossos programas

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são cidadãos de Primeira Classe (First Class Citizen)

"""

# Exemplo - Definindo as funções:

from typing import Callable
from random import choice


def somar(a: int, b: int) -> int:
    """Função soma."""
    return a + b


def subtrair(a: int, b: int) -> int:
    """Função subtração."""
    return a - b


def calcular(num1: int, num2: int, funcao: Callable[[int, int], int]) -> int:
    """Função que recebe uma função para cálculo."""
    """Obs: o Callable é chamado como retorno de qualquer coisa "chamável", sej
    função ou outro. Ele recebe [[argumentos], tipo de retorno]"""
    """No retorno geral da função temos o tipo de retorno que a função
    chamada retorna, no caso int."""
    """Obs: D´úvidar ver Pep 612 e pep 484"""
    return funcao(num1, num2)


print(calcular(5, 4, somar))
print(calcular(10, 2, subtrair))

# Nested Functions - funções aninhadas:

# Em Python podemos tbm ter funções dentro de funções, que são conhecidas por
# Nested Functions ou tbm Inner Functions (Funções internas):


# ex:
def cumprimento(pessoa: str) -> str:
    """Função dentro de função, exemplo."""
    def humor():
        return choice(('Hey', 'Saia', 'Every day seems a little better'))
        # Escolhe aleatoariemnte uma das strings
    return humor() + ", " + pessoa


print(cumprimento("Gere"))


# Retornando funções de outras funções:

def faz_me_rir() -> Callable[[], str]:
    """Funções de outras funções, retornando a função."""
    def rir() -> str:
        return choice(('hahahaha', 'kkkkkkk', 'sjhajshajsahj'))
    return rir  # Estamos retornando a função


rindo = faz_me_rir()
print(rindo())


# inner Functions (Nested functions) podem acessar o escopo mais externo:

def make_me_laugh(pessoa: str) -> Callable[[], str]:
    """Agora testando o acesso de uma variável externa por uma função mais
    externa, o que é plenamento possível."""
    def laughing() -> str:
        risada = choice(('saasgysagysa', 'ahsudhaveditahsuahsua'))
        return f'{risada}, {pessoa}'
    return laughing


rindo = make_me_laugh('Gere')
print(rindo)