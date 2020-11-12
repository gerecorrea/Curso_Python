import matplotlib.pyplot as plt  # rename as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 3, 4, 7, 9, 7, 10, 8]

# Definido título do gráfico
plt.title("Título do meu gráfico")  # define o título

# Definindo nome aos eixos do gráfico:
plt.xlabel("Eixo X")  # eixo x
plt.ylabel("Eixo Y")  # eixo y

plt.plot(x, y)  # plot que recebe dois parametros de lista

plt.show()  # mostra o gráfico e mtela

