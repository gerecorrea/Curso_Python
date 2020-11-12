"""

Counter, do módulo collections.

Collections -> High-performance container datatypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo
Collection  Counter que é parecido com um dicionário, contendo como chave o
elemento da lista passada como parâmetro e como valor a quantidade de
ocorrências desse elemento.

"""

# Import do Counter
from collections import Counter

lista = {1, 1, 1, 2, 2, 2, 6, 6, 4, 3, 2, 1, 9, 5, 3, 2, 1, 4, 6, 5, 3}

# Utilizando o Counter:

# Ex 1 - contando repetições de numeros
res = Counter(lista)
print(res)  # Retorna a quantidade de ocorrências para cada valor
# Tá retornando errado, 1 ocorrência de cada

# Ex 2 - Contando ocorrência de letras/caracteres
print(Counter('Geremias Correa'))

# Ex3 - 
texto = """ Escalação do Athletico atual: Santos, Jonathan, Thiago heleno
Felipe Aguilar, Abner Vinicius, Christian, Erick, Leo Cittadini, Jorginho
Nikão, Renato Kayzer. Essa foi a escalação do Athletico"""
print(Counter(texto))  # Conta os caracteres
# Repare que ele diferencia maiúsculas de minúsculas, acentuações, etc
# Caso queira unificar, basta usar outros métodos e unificar

palavras = texto.split()
print(Counter(palavras))  # Agora conta as palavras em si

# Pegar as x palavras mais comuns especificadas:

res = Counter(palavras)
print(res.most_common(5))  # Pega a 5 palavras de maior ocorrência
# Caso empate, acho que pega pela ordem disposta
