"""Sorted.

Não confundir com a função sort, apesar do nome.

O sort() só funciona em listas, o sorted pode ser usado com qualquer iterável
    Listas, tuplas, dict, etc

O sorted() serve para ordenar quasiquer elementos
    Você pode transformá-los em outros sem problemas, caso queira

Mas cuidado:
    O sorted (diferente do sort) não altera a própria lista
    Mas sim gerá uma nova lista reotrnada ordenada
    Essa lista nova precisa ser atribuída a algum elemento
    Se não ela não funciona.

"""

numeros = (6, 1, 8, 2)
new = sorted(numeros)
print(new)

# Parâmetros para o sorted():

print(sorted(numeros, reverse=True))  # Ordena descrecente, está invertido

print()

# utilizando o sorted() para coisas mais complexas:

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "eu adoro pizzas"]},
    {"username": "Felipe", "tweets": ["Eu odeio casas"]},
    {"username": "Bruno", "tweets": [], "cor": "amarelo"},
    {"username": "Rodrigo", "tweets": ["Eu adoro carros", "eu adoro pizzas"]},
    {"username": "Bruno", "tweets": [], "cor": "preto", "musica": "rock"},
]

print(sorted(usuarios, key=len))  # Essa já seria a ordenação padrão
print(sorted(usuarios, key=lambda x: x["username"]))  # por ordem alfabética

# Orndenado pelo numero de tweets:
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']), reverse=True))

# ùltimo exemplo:

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Skald and Shadows", "tocou": 7},
    {"titulo": "Valhalla", "tocou": 5},
    {"titulo": "Frozen", "tocou": 1},
    {"titulo": "It's a Long Way to the Top if you Wanna Rock n' Roll", "tocou": 4},
]

print(sorted(musicas, key=lambda musica: musica['tocou'])) # tocadas crescente
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True)) # dec
print(sorted(musicas, key=lambda musica: musica['titulo'])) # crec alfabetica