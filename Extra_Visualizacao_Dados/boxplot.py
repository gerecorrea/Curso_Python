# construir os gráficos de diagrama de caixa

"""Lembrando que é um diagrama de dispersão, onde:
temos na linha central a mediana
O topo da caixa é o terceiro quartil, a base da caixa o primeiro quartil
O risco superiores e inferiores os máximos e mínimo
Pontos fora são os outliers

"""

import matplotlib.pyplot as plt
import random

vetor = []
for i in range(1000):
    numero_aleatorio = random.randint(10, 1000)
    vetor.append(numero_aleatorio)


plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()