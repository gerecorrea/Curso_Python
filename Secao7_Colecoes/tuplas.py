"""

Tuplas (tuples).

Tuplas são representadas por parenteses, diferentemente das listas
Tuplas são imútaveis
    Toda alteração em uma tupla, gera uma nova tupla
    Ou seja, caso vá fazer alguma operação sobre ela (sort ou add elemento)
        Precisa atribuir a outra tupla

Por serem imútaveis, elas são mais rápidas que listas
Também deixam seu código mais seguro, dado a imutabilidade delas

Ela tem dois métodos propriamente dela para uso: index e count

Obs: apesar da existência delas, as named tuples parecem bem melhores que essa
    Se aproximam mais da ideia de struct e representam simplificada

"""

# Cuidado 1: são representadas por parentêses, porém sua declaração varia:

tupla = (1, 2, 3, 4, 5, 6, 7)
tupla2 = 1, 2, 3, 4, 5  # Também identifica como tupla
print(type(tupla))

# Cuidado 2: Tuplas com um elemento são bem específicas:
tupla3 = (4,)  # ou = 4,

# Gerando uma tupla de forma rápida:
tupla = tuple(range(15))  # Gera uma tupla de 0 a 14
print(tupla)

tupla_ex = ('Geremias', 'Correa')
nome, sobrenome = tupla_ex
print(nome, sobrenome)

# Soma, máx, min, tamanho, cont (padrão listas):
# novamente, somente caso sejam toda de inteiros
tupla3 = (1, 2, 3, 4, 5, 6)
print("Soma tupla3:", sum(tupla3))
print("Máx tupla3:", max(tupla3))
print("Min tupla3:", min(tupla3))
print("Tam tupla3:", len(tupla3))
print("Qtd de 3 na tupla3: ", tupla3.count(3))

# Concatenação de tuplas (padrão listas):
tupla4 = (1, 2, 3)
tupla5 = (4, 5, 6)
tupla6 = tupla4 + tupla5  # Repare que atribui a uma nova
# Poderia também sobreescrever a uma mesma variável, como abaixo
tupla4 = tupla4 + tupla5
print(tupla6)
print(tupla4)
print(6 in tupla6)

# Iterando sobre uma tupla (padrão listas):
for n in tupla6:
    print(n, end=' ')
print()

for indice, valor in enumerate(tupla6):
    print(f'Tupla {indice} = {valor}', end=' // ')
print()

# Dicas para utilização de tuplas:

# Devemos utilizá-las quando não precisamos modificar os dados em uma coleção

# Ex1:
meses = ('Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out')
# Repare que não iremos modificar a lista/tupla de meses
print(meses)
print(meses.index('Out'))

# Slicing (padrão listas):
# tupla(inicio:fim:passo)
print(meses[2:11:2])  # Passou do limite válidd, mas não é problema

# Copiando uma tupla para outra (padrão listas):
# Em tuplas não temos o problema de shallow copy, dado a imutabilidade
tupla7 = [1, 2, 3]
tupla8 = [5, 6, 7]
tupla9 = tupla7
