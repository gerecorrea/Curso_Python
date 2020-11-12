"""Reversed.

OBS: não confunda com a função reverse() que estudamos nas listas
    reverse() é uma função das listas somente
    A relação é parecida com sort() e sorted()

Sua função é inverter o iterável

A função reversed() retorna um iterável chamado List Reverse Iterator
    Pode usar em list, tuple, set, dicionário, range, etc

"""

lista = [1, 2, 3, 4, 5]

# Lista:
print(list(reversed(lista)))

res = tuple(reversed(lista))
print(res)

# Podemos iterar sobre o reversed:
for letra in reversed('Geremias Corrêa'):
    print(letra, end='')
print()

# Podemos fazer o mesmo sem uso do for:
print(''.join(list(reversed('Geremias Corrêa'))))
# Com o join transformamos a lista de string em uma string novamente.

# Mais simples ainda usando o slice de strings:
print('Geremias Corrêa'[::-1])

# Usar o reversed para fazer um laço inverso:
for n in reversed(range(0,10)):
    print(n, end=' ')
print()
