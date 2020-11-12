"""Generators.

O que seria o "tuple comprehension" é chamado de generator expression
    Por isso tal coisa não foi estuda no collections

Sintaxe:
    Igual ao de list, mas ao invpes de [] usa ()
    Ou seja, deixar tudo entre () indica estar usando generators

A partir de conversão e uso, aqui o dado tbm é apagado da memória

Seu uso é preferível ao uso do List Comprehension, por exemplo
"""
# Import para uso em um ex, retorna a qtd de bytes em memória do elemento
from sys import getsizeof

# Aquela verificação da aula passada, sobre se algum nome começa com 'C'
# Poderia ter sido feita com generators

nomes = ['Carlos', 'Mathilda', 'Leon', 'Julius', 'Carlinhos Bala', 'Vincent Vega']

print(tuple(nome[0] == 'C' for nome in nomes))
# Caso fizesse como list comprehension, bastava fazer em []
# Neste caso, estamos retorna True ou False por conta da condição solicitada

# Mostrando quanto bytes a string x está ocupando em memória:
x = "Nanananananana Na Beatles"
print(getsizeof(x))
print(getsizeof(int))
print(getsizeof(90))
print(getsizeof(float))
print(getsizeof(str))
print(getsizeof(bool))

# Gerando uma lista de números com List Comprehension:

list_comp = getsizeof([x * 10 for x in range(1000)])

# Genraod uma lista de num com set comprehension: 
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando umma lista de num com dictionary comprehension:
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista com generator:
gen_comp = getsizeof(x * 10 for x in range(1000))

print(f"Size list 1000: {list_comp} bytes")
print(f"Size set 1000: {set_comp} bytes")
print(f"Size dictionary 1000: {dict_comp} bytes")
print(f"Size Generator 1000: {gen_comp} bytes")

# REPARE QUE CONSOME ABSURDAMENTE MENOS MEMÓRIA!!
# Isso porque ele não gera automaticamente, só gera realmente quando for
# realmente utilizar
# O set e o dict ocupam mais por conta da questão de evitar repetição e
# chaves únicas, respectivamente. São classes mais complexas

# Iterando no Generator Expression:
gen = (x * 10 for x in range(1000))

for num in gen:
    print(num, end=' ')