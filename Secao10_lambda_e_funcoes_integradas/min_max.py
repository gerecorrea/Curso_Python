"""
Min e Max

min() -> retorna o menor valor em um iterável ou entre dois elementos

max() -> retorno o maior valor em um iterável ou entre dois elementos

"""

# Ex retomando:
conjunto = {1, 23, 87, 92, 3, 12, 54, 2, 7, 5}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 12, 'd': 7, 'e': 4}
print(max(dicionario.values()))

# Programa que recebe dois valores e mostra o maior:
# val1 = int(input('Informe o primeiro valor: '))
# val2 = int(input('Informe o segundo valor: '))
# print(max(val1, val2))

# AAAAAAAAAAaaaaaaaaaa1!

# Min mesmo esquema mais inverso.
# min()
# print(min(val1, val2))

# Exemplos mais complexos:

nomes = ["Arya", "Smason", "Stinson", "Joey", "Dexter", "Parararara"]
print(max(nomes))  # pega o nome por ordem alfabética maior (ascii)
print(min(nomes))  # pega o nome por ordem alfabética menor (ascii)
print(max(nomes, key=lambda nome: len(nome)))  # Nome mais longo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Skald and Shadows", "tocou": 7},
    {"titulo": "Valhalla", "tocou": 5},
    {"titulo": "Frozen", "tocou": 1},
    {"titulo": "It's a Long Way to the Top if you Wanna Rock n' Roll", "tocou": 4},
]
print(max(musicas, key=lambda musica: musica['tocou']))  # pega a que mais tocou
print(min(musicas, key=lambda musica: musica['tocou']))  # pega a que menor tocou

# Desafio imprima somente o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])  # imp titulo
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])  # imp titulo

# Desafio encontrar a mais/menos tocada sem o max ou min:
maximo = 0
for musica in musicas:
    if musica['tocou'] > maximo:
        maximo = musica['tocou']
        nome_musica = musica['titulo']
print(nome_musica)
# Obs: bem simples, padrao lógica de outra linguagem.