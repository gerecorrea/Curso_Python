"""

Mapas -> Conhecidos em Python como dicionários.

São representados por chaves, assim como dicionários.

Ele nomeou a aula de mapas, mas é claramente continuação de dicionários
    Botei dicionário2

Aqui vemos um pouco de como iterar sobre dicionários
Também de desempacotar/aplicar sobre funções inerentes ao Python
    Máx, Min, Sum, Tam.
"""

receita = {'jan': 100, 'fev': 250, 'mar': 200}

# Iterar sobre dicionários:
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'{chave} : {receita[chave]}')

print(receita.keys())  # Retorna as keys do dicionário

for chave in receita.keys():  # Método recomendado de iterar sobre chaves
    print(receita[chave])

print(receita.values())
for valor in receita.values():  # Método recomendado de iterar sobre valores
    print(valor)

# Desempacotamento de dicionários:
for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

# Soma, máx, min, tamanho:
print(sum(receita.values()))  # Pega diretamente os valores e os soma
print(max(receita.values()))  # Pega diretamente o valor max
print(min(receita.values()))  # Pega diretamente o valor min
print(len(receita))  # Pega o tamanho
