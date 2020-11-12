"""

Named Tuples, o módulo collections

Recap tupla:
tupla = 1, 2, 3

É uma ideia de "tupla nomeada", são tuplas diferenciadas, em que especificamos
um nome para a mesma e também parâmetros

Fica bastante próximo de uma ideia de struct de C e tal, porém modificado no acesso
Pois você define nome e todos os tipos dentro


"""

# Importando
from collections import namedtuple

# Definindo nome e parametros:

# Forma 1 de declaração
cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 de declaração
cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 de declaração - melhor método
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando:

ray = cachorro(idade=2, raca='Chow Chow', nome='Ray')  # Instanciando um cach.
print(ray)

# Acessando os dados

# Forma 1 (ruim)
print(ray[0])  # índice da idade

# Forma 2 (melhor)
print(ray.idade)
print(ray.nome)
