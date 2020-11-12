"""Any e All.

Utilizando aqui o list comprehension

all() -> retorn True, se todos elementos do iterável satisfazem a condição
    Se o iterável é vazio,a automaticamente satisfaz e retorna True

any() -> retorna True se algum dos elementos iterados satisfazem a condição
    Se o iterável é vazio, tbm retorna True
"""

# Exemplo all():
print(all([0, 1, 2, 3, 4, 5]))  # 0 é False
print(all([1, 2, 3, 4]))
print(all(['gg', 'fabainski', True, '2']))

nomes = ['Carlos', 'Camarão', 'Cláudia', 'Carmen']
nomes2 = ['Carlos', 'Camarão', 'Cláudia', 'Carmen', 'Pedro', 'Thiago']
print(all([nome[0] == 'C' for nome in nomes]))  # Se todos começam com 'C', true
print(all([nome[0] == 'C' for nome in nomes2]))  # Se todos começam com 'C', false

# se algumas das letras estover na str, ou mesmo lsita vazia, retorna true
print(all(letra for letra in 'eou' if letra in 'aeiou'))  # Todas estão na str

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
print(all([num for num in [4, 2, 10, 0, 8] if num % 2 == 0])) 
# Tenho a impressão que o 7 ali era pra fazer retornar False

# Any():

print(any([0, 1, 2, 3]))
print(any([0, 0, 0, 0]))

# O esquema é mto similar ao all(), apenas aceita caso um já satisfaça