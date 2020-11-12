"""Set Comprehension."""

"""
Lembrando que set é definido por {} e não tem valores repetidos nem ordenação

"""

# Exemplo 1:

numeros = {num for num in range(1, 7)}
print(numeros)

# Exemplo 2:

numeros = {num ** 2 for num in range(0, 10)}
print(numeros)  # Repare que é fora de ordem, pq tanto faz

# Desafio - faça uma alteraçã na estrutura acima para gerar um dicionário:

numeros_dic = {num: num ** 2 for num in range(0, 10)}
print(numeros_dic)
# Obs: apenas adicionamos a chave com "num:"

# Exemplo 3 - com string:

letras = {letra for letra in 'Geremias Corrêa'}
print(letras)  # Deve gerar: 'G', 'e', 'r',... mas fora de ordem e sem repet.
