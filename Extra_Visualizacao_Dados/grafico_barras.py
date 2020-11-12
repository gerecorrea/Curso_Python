import matplotlib.pyplot as plt  # rename as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 3, 4, 7, 9, 7, 10, 8]

titulo = "Gráfico de barras"
eixox = "Eixo x"
eixoy = "Eixo y"


# Definido título do gráfico
plt.title(titulo)  # define o título

# Definindo nome aos eixos do gráfico:
plt.xlabel(eixox)  # eixo x
plt.ylabel(eixoy)  # eixo y

plt.bar(x, y)  # Aqui que muda, teremos assim um gráfico de barras.

plt.show()  # mostra o gráfico e mtela

