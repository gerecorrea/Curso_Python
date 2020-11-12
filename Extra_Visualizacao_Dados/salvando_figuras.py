import matplotlib.pyplot as plt  # rename as plt


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 3, 4, 7, 9, 7, 10, 8]

plt.title("Título do meu gráfico")  # define o título

# Definindo nome aos eixos do gráfico:
plt.xlabel("Eixo X")  # eixo x
plt.ylabel("Eixo Y")  # eixo y

# Utilizando marcadores e modificadores para os gráficos:

plt.plot(x, y, color="#090000", linestyle=":")
# Isso aqui abaixo para o scatterplot, não necessariamente para os outros
plt.scatter(x, y, label="Meus pontos", color="m", marker="h", s=200)  # plot que recebe dois parametros de lista
# com o label adc na identificação por cor dos pontos/dados gerados
# marker é o argumento que modifica o tipo de marcador de cada ponto
# s é o argumento que modifica o taamnho dos pontos plotados. 

plt.savefig("figura.png", dpi=300) # png de baixa resolução, podemos setar o dpi para ajudar.
plt.savefig("figura.pdf") # melhor resolução
plt.show()  # mostra o gráfico e mtela
