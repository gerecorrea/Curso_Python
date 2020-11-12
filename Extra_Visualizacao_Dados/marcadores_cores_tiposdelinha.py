import matplotlib.pyplot as plt  # rename as plt

# link com os tipos de marcadores etc:
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html 


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 3, 4, 7, 9, 7, 10, 8]
z = [20, 5, 400, 100, 50]  # criado para dmeonstração, se fizer "s=z" no plot, temos que o tamanho dos pontso será baseado nisso aqui

# Definido título do gráfico
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

plt.show()  # mostra o gráfico e mtela

"""
Markers
character 	description
'.' 	point marker
',' 	pixel marker
'o' 	circle marker
'v' 	triangle_down marker
'^' 	triangle_up marker
'<' 	triangle_left marker
'>' 	triangle_right marker
'1' 	tri_down marker
'2' 	tri_up marker
'3' 	tri_left marker
'4' 	tri_right marker
's' 	square marker
'p' 	pentagon marker
'*' 	star marker
'h' 	hexagon1 marker
'H' 	hexagon2 marker
'+' 	plus marker
'x' 	x marker
'D' 	diamond marker
'd' 	thin_diamond marker
'|' 	vline marker
'_' 	hline marker
"""

"""
Line Styles (linestyle)
character 	description
'-' 	solid line style
'--' 	dashed line style
'-.' 	dash-dot line style
':' 	dotted line style
"""

"""
Colors
Obs: aceita hexadecimal tbm, sem problemas.

The supported color abbreviations are the single letter codes
character 	color
'b' 	blue
'g' 	green
'r' 	red
'c' 	cyan
'm' 	magenta
'y' 	yellow
'k' 	black
'w' 	white
"""