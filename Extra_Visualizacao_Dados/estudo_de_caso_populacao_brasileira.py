# analisando o crescimento da população brasileiro - datasus
# Utilizando o arquivo .csv salvo na pasta
    # o arquivo csv atual está separado os dados por ";"


import matplotlib.pyplot as plt


dados = open("populacao_brasileira.csv").readlines()

x = []  # armazena os anos
y = []  # armazena a população

for i in range(len(dados)):
    if i != 0:  # ignora a primeira linha, cabeçalho
        linha = dados[i].split(";")
        x.append(int(linha[0]))  # ano
        y.append(int(linha[1]))  # população

plt.bar(x, y, color="#04e4e4")
plt.plot(x, y, color="k")

plt.title ("Crescimento da população Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População (em milhões de pessoas)")

plt.show()

plt.savefig("populacao_brasileira.png", dpi=300)