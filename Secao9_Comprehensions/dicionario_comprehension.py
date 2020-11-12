"""Dictionary Comprehension."""

""" 
Comprehension com uso em dicionários

Pense no seguinte:
tupla é (), lsita é [], set é {}

Mas dicionário tem chave e valor:
dicionario = {'a': 1, 'b': 2}

Sintaxe:
    {chave:valor for valor in iterável}
    Em lista seria [valor for valor in iterável]
"""

# Exemplo 1:

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)
# Obs: não modificamos, mas poderíamos ter tbm modificado a chave

# Exemplo 2 - gerando um dicionário ao quadrado a partir de uma lista:

lista = [1, 2, 3, 4, 5]
quadrado_2 = {valor: valor ** 2 for valor in lista}
print(quadrado_2)

# Exemplo 3 - querendo misturas as chaves com valores em um dictionary:

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo 4 - Com lógica condicional:

numeross = [1, 2, 3, 4, 5]

res = {num: 'par' if num % 2 == 0 else 'impar' for num in numeross}
print(res)
# Obs: pode colocar entre parentes a condicional, como abaixo:
# res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeross}