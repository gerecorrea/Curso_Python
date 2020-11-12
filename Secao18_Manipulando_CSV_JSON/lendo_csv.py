"""
Lendo arquivo CSV

CSV - Comma Separated Values

Apesar disso, podem ser separados por outro caractere:
    vírgula(,), ponto e vírgula (;), espaço ( ), 

No arquivo que estamos usando, temos um cabeçalho, mas nem sempre há.

site para conseguir dados (para teste, etc):
dados.gov.br/dataset

Podemos ler do jeito padrão, mas não é o ideal, o ideal é:
    Via reader -> permite que iteremos osbre as linhas do arquivo csv como listas
    Via DictReader -> mesmo do anterior, mas como OrderedDicts

"""
from csv import reader
from csv import DictReader


# Forma não ideal:

with open('lutadores.csv', 'r+') as arquivo:
    dados = arquivo.read()
    # print(type(dados))
    print(dados)
    print("\nDe forma diferente, com uso do split:")
    dados = dados.split(',')[3:]  # Com o 3: eliminamos o cabeçalho, pq são 3
    # dados nela.
    print(dados)

# Forma ideal 1 - Com o reader - pega linha a linha como lista:
with open('lutadores.csv', 'r+') as arquivo:
    leitor_csv = reader(arquivo, delimiter=',')  # Devolver um iterator
    # por padrão o delimitador já é a vírgula, então não precisava botar
    next(leitor_csv)  # Pula o cabeçalho (no caso uma linha ele pula)
    print("\nAgora printando com o uso do reader e trabalhando com esses dados:")
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f"{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]} cm.")

# Forma ideal 2 - com o DictReader
with open ('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')  # por padrão já era a virg
    print("\nAgora com o dictReader:  ")
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a) {linha['País']} e mede "
            f"{linha['Altura (em cm)']}"
        )
        # Transformo num dict de acordo com as chaves dadas no cabeçalho
        # Bem útil tbm.
        # automaticamente excluí o cabeçalho