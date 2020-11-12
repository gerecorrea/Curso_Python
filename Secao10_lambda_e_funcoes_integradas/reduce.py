"""Reduce.

Obs: a partir do Python3+ o reduce() não é mais uma função integrada (builtin)

Agora, para usar, é necessário utilização o módulo functools

Ela foi retirada pois um loop for é 99% das vezes mais legível e faz o mesmo

Para entender o reduce():

Dado uma coleção de dados (ex), temos uma função que recebe dois parâmetros
A função reduce() irá:
    receber dois parâmetros, a função e o iterável (iguais os outros)
    aplica a função a o resultado e chama o próximo item iterável e o resultado
    Mesma ideia do js

    Seria na prática algo como:
    funcao(funcao(funcao(funcao(a1,a2),a3), a4), an) 

"""

from functools import reduce

# Vamos utilizar a função reduce() para multiplicar os dados de uuma lsita:

dados = [2, 3, 5, 6, 7, 8, 9, 10, 13]

# Para utilizar p reduce() nós precisamos de uma funçaõ que recebe dois param.

multi = lambda x, y: x * y  # Aqui precisa ter dois parâmetros

res = reduce(multi, dados)
print(res)

# Fazendo isso com o for - preferível!!!:
res = 1
for n in dados:
    res *= n
print(res)