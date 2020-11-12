"""
Entendendo iterators e iterables.

Iterator ->
    Objeto que pode ser iterado
    Objeto que retorn um dado, sendo um elemento por vez quando uma função 
    next() é chamada

Iterable -> Objeto que irá retornar um iterator quando a função iter() for cham
"""

nome = "Geek"  # É um iterable mas não é um iterator
numero = [1, 2, 3, 4, 5]  # É um iterable mas não é um iterator

# Para tonrá-lo iteráveis:
it1 = iter(nome)
it2 = iter(numero)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

# Ele faz o controle automático pra gente de um for iterável, por exemplo