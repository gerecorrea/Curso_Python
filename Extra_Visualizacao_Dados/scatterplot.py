# Também conhecido como gráfico de dispersão

import matplotlib.pyplot as plt  # rename as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 3, 4, 7, 9, 7, 10, 8]

titulo = "Scatterplot"
eixox = "Eixo x"
eixoy = "Eixo y"


# Definido título do gráfico
plt.title(titulo)  # define o título

# Definindo nome aos eixos do gráfico:
plt.xlabel(eixox)  # eixo x
plt.ylabel(eixoy)  # eixo y

plt.scatter(x, y, label="Meus pontos", color="red")  # Aqui que muda, teremos assim um gráfico scatterplot
# repare que foi selecionada cor vermelha.
# plt.plot(x, y)  # se ativasse, plotaria as linhas ligando os pontos tbm
plt.legend()

plt.show()  # mostra o gráfico e mtela

