"""Filter.

Selecionar (filtrar) certo grupo de dados em uma coleção

Ela recebe dois parâmetros (assim como map):
    O primeiro é uma função
    O segundo o iterável

Após serem utilizados, os dados do filter tbm são excluídos (como no map)

Ela não modifica os valores, apens os seleciona ou não e atribui a alguma lista

"""
# Bib para dados estatisticos
import statistics  # Bib para dados estatisticos

# Dados coletas de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, -0.1]

# Calculando a media utilizando mean:
print(statistics.mean(dados))

# Agora entra o Filter:

# Vamos selecionar apenas os dados acima da média:

media = statistics.mean(dados)
res = filter(lambda valor: valor > media, dados)
print(list(res))

# Remoção de dados faltantes com filter:

paises = ['', 'Argentina', 'Brasil', '', 'Chile', '', 'Venezuela', 'Equador', '']

res = filter(None, paises)  # Faz com que o '' sejam filtrados
print(list(res))

# Ou tbm por
res = filter(lambda pais: len(pais) > 0, paises)  # Lógica mais legível
# res = filter(lambda pais: pais != '', paises)  # Outra forma
print(list(res))

# Exemplo mais complexo:

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "eu adoro pizzas"]},
    {"username": "Felipe", "tweets": ["Eu odeio casas"]},
    {"username": "Rodrigo", "tweets": ["Eu adoro carros", "eu adoro pizzas"]},
    {"username": "Bruno", "tweets": []},
]

# vamos filtrar os usuários inativos no twitter (não twittou)

inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)
# Pegou somente os inativos (bruno)

# forma 2 de realizar essa filtragem dos inativos
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)


# Combinar filter() com map():
nomes = ['Vanessa', 'Ana', 'Maria', 'Dora', 'Jaque', 'Clotilde', 'Bia', 'Gabi']
# Devemos criar uma lista contendo dado, desde que cada nome tenha menos 5 caracteres

lista = list(map(lambda nome: f"Sua instrutora é {nome}", filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
# Repare que no primeiro parametro passou a função lambda para modificação
# No segundo foi a lista para ser utilizada, sendo nela realizado o filtro, tbm usando lambda