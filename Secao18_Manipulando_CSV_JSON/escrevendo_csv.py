"""
Escrevendo em arquivos CSV

Temos a mesma ideia que na leitura, utilização de duas formas:
    writer() -> utiliza um escritor para csv
        writerow() -> escreve uma linha
    DictWriter -> Utiliza um dicionário para escrever


A forma de abertura varia conforme o contexto, aqui foi usado w por exemplific

"""

from csv import writer
from csv import DictWriter

# Escrevendo utilizando o writer():

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])  # Header
    # Se for utilizar um arquivo já criado, ele vai reescrev. o header
    while filme != 'sair':  # While is not 'sair'
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input('Informe o genero: ')  # input
            duracao = input("Informe a duração (em minutos): ")  # input
            escritor_csv.writerow([filme, genero, duracao])  # Write in the csv

# Escrevendo utilizando o DictWriter():
# OBS: as chaves do dicionário devem ser exatamente as mesmas que as do cabeçalho
with open('filmes2.csv', 'w') as arquivo:
    print("\nAgora inserindo dados via DictWriter: ")
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)  # Passo a lista
    escritor_csv.writeheader()  # Colomamos o header
    filme = None
    while filme != 'sair':  # While is not 'sair'
        filme = input("Informe o nome do filme: ")
        if filme != 'sair':
            genero = input('Informe o genero: ')  # input
            duracao = input("Informe a duração (em minutos): ")  # input
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})  # Write in the csv
            # Para escrever a linha utiliza o writerow igual anteriormente.
