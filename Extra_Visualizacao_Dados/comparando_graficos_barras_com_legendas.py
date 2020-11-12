import matplotlib.pyplot as plt  # rename as plt

x = [1, 3, 5, 7, 9,]
y = [7, 9, 7, 10, 8]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 3, 4, 7, 8]

titulo = "Gráfico de barras"
eixox = "Eixo x"
eixoy = "Eixo y"

# Definido título do gráfico
plt.title(titulo)  # define o título

# Definindo nome aos eixos do gráfico:
plt.xlabel(eixox)  # eixo x
plt.ylabel(eixoy)  # eixo y

# Plot com legendas:
plt.bar(x, y, label = "Grupo 1")  # Aqui que muda, teremos assim um gráfico de barras.
plt.bar(x2, y2, label = "Grupo 2")  # Lança de forma comparatível 
plt.legend()

plt.plot

plt.show()  # mostra o gráfico e mtela

