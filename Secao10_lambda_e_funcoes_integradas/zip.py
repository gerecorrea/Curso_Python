"""Zip.

zip() -> cria um iterável chamado "zip object", que agrega elementos de cada
um dos iteráveis passados como entrada em pares

ELe é destruído após a primeira utilização 

Assim como para os outros, com ele podemos criar lists, tuples, set, dict, etc

O zip utiliza como parâmetro o menor tamanho em iterável. Para neste ponto.
    Independente da poisção de cdda um deles nos argumentos
"""

# Exemplos:

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2, 'abc')

print(zip1)  # retorna zip object
print(list(zip1))  # Pegou o mesmo elemento de cada e formou pares com eles
print(set(zip1))  # Aqui ela já tá destruída, pois já foi usada
print(dict(zip1))

# Iterando com o zip:

tupla = 1, 2, 3, 4, 5
lista = [7, 6, 9, 4, 5, 3]
dicionario = {'a': 1, 'b': 3, 'c': 7, 'd': 9}

zt = zip(tupla, lista, dicionario.values())
print(tuple(zt))

# Lista de Tuplas:

dados = [(0, 1), (2, 3), (5, 6), (6, 7)]
print(list(zip(*dados)))  # Preisa usar o * nesse caso

# Exemplos mais complexos:

prova1 = [80, 91, 78]
prova2 = [73, 94, 52]
alunos = ['maria', 'pedro', 'fabio']

# Pegou a maior nota de cada aluno de forma simples
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)
# dado 0 a 3 por conta de serem elementos do for
# dado[0] é a chave, os outros dois são valor (ficam depois do :)
# itero sobre o zip passandoss os 3 dados como parametro

# Utilizar o map para fazer o mesmo acima junto do zip:
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
# Foi feito um zip dos alunos como primeiro elemento e a nota o segundo
# Nesse segundo criamos um map, que tem então 2 parametros
# No primeiro chamamos uma funçaõ lambda que pega a maior nota
# no segundo é o objeto iterável, que são as duas provas.
