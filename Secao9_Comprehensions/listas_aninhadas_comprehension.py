"""Listas aninhadas (Nested Lists)."""

"""
Algumas linguagens de programação (C/Java) possuem estruturas de dados array
    Unidimensionais seriam os arrays e multidimensionais as matrizes

Em python se tem as listas, ao invés disso.
    Mais flexíveis nos dados e no tamanho

# Repare que a construção de um loop duplo com uso do comprehension é:
# [[for mais inteiro] for mais externo]
"""

# Exemplo 1:

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Seria uma matriz 3x3

# Acesso de dados:
print(listas)  # Printa completa
print(listas[0])  # Printa a linha 0 (lista interna 1)
print(listas[0][2])  # Linha 0 e coluna 2

# Iterando com loops em uma lista aninhadas (duplo loop):
for lista in listas:
    for num in lista:
        print(num, end=' ')
    print()

# List Comprehension nesse contexto acima de impressão do ex 1:
[[print(valor, end=' ') for valor in lista] for lista in listas]
print()
# Repare que a construção é [[for mais inteiro] for mais externo]

# Exemplo 2 - gerando um tabuleiro/matrix 3x3:

tabuleiro = [[numero for numero in range(1, 4)] for _ in range(1, 4)]
print(tabuleiro)

# Exemplo 3 - gerando jogadas para um jobo da velha:

velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for _ in range(1, 4)]
print(velha)

# Exemplo 4 - gerando valores iniciais:
print([['*' for _ in range(1, 4)] for _ in range(1, 4)])