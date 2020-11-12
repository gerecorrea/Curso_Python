"""Map (mapeamento) em Python.

Com map fazemos o mapeamento de valores para função

Sintaxe:

    map(funcao, dados)

    O map object (retorno) é do tipo: f(a1), f(a2), f(a3), ...

Ele mapeia uma entrada de dados sobre uma função de maneira mais prática
Os resultados são colocados pro dado atribuído (lista, etc)
Ele busca alterar o dado em si

O map se autodestroi (seu valores, limpando a memória) após a primeira
utilização do valor da variável ao qual este foi atribuído

"""

import math


def area(raio: float) -> float:
    """Calcula a área de um círculo com raio r."""
    return math.pi * (raio ** 2)


print(area(2))
print(area(5.3))

# Forma 1 - mapeando de maneira apenas lógica sem uso de nada:
areas = []
raios = [2, 5, 7.1, 9, 10.5]
for r in raios:
    areas.append((area(r)))
print(areas)

# Forma 2 - de mapear essas áreas com uso do map somente:
areas2 = map(area, raios)
print(list(areas2))  # Se não converter para uma lista, ele retorna só map obj
# Ele mapeia uma entrada de dados sobre uma função de maneira mais prática
# Os resultados são colocados pro dado atribuído, nesse caso uma lista

# Forma 3 - usando map para mapear e com lambda:
print(list(map(lambda r: math.pi * (r ** 2), raios)))  # mto direto

# Obs: após utilizar a função map, após a utilização do resultadom ele zera

# Outro exemplo - lista de cidades com temperaturas em ºC para F:
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 26), ('Tóquio', 21)]

c_para_f = lambda dado: (dado[0], round((9/5) * dado[1] + 32, 2))
print(list(map(c_para_f, cidades)))
# Nesta função, mapeamos cada dado da cidade, tq o dado é composto por:
# elemento 0 seria o nome da cidade, e o 1 a temperatura em ºC
# Com isso, mapeamento na função criada (c_para_f), pegando esse dado