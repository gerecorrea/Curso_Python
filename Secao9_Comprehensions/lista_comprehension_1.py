"""
List Comprehension parte parte 1

Utilizando list compreehension nós podemos gerar novas listas com dados
processados a partir de outro iterável

A sintaxe da lista comprehension:
    Com é lista, delimita por colchetes []

    Ex:

    [dado for dado in iterável]

Mas para entender melhor o que está acontecendo, a expressão deve ser dividida
em duas partes:
    Primeira parte: for numero in numeros
    Segunda parte: numero * 10
"""

# Exemplo aplicado 1:
numeros = [1, 2, 3, 4, 5]

# Nesta mapeamos a lista para todo valor ficar ele mesmo * 10
res = [numero * 10 for numero in numeros]
# res = [numero * 10 for numero in [1, 2, 3, 4, 5]]  # aceita a lista em si

print(res)
# Obs: poderia ter feito isso com um loop comum, usando outra lista

# Exemplo aplicado 2:

name = 'Geremias Corrêa'

print([letra.upper() for letra in name])


# Exemplo 3:

def caixa_alta(nome: str) -> str:
    """d."""
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'felipe', 'cristiano']
print([caixa_alta(amigo) for amigo in amigos])

# Exemplo 4:

# Transforma em valores booleanos os valores contidos na lista
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# Exemplo 5:

print([str(numero) for numero in [1, 2, 3, 4, 5]])
