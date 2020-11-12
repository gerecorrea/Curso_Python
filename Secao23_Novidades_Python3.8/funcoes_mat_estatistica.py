"""

Novos recursos de matemática e estatística

"""

# MATH:

# math.prod - retorna o produto de um container
#math.isqrt - tira a raiz com valor inteiro (trunca)
# math.dist - retorna a distancia euclidiana entre dois pontos
    # serve tanto para 2d quanto 3d. Recebe um container de 3 valores.
# math.hypot - retorna a hipotenusa/norma euclidiana. recebe um conteiner
import math

nums_v1 = [2, 3, 6, 8]
nums_v2 = (2, 3, 5, 7)

print(math.prod(nums_v1))

print(math.isqrt(9))
print(math.sqrt(25))

# pontos 3d:
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# pontos 2d:
p2d1 = [12, 50]
p2d2 = [43, 3]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

# O asterisco é obrigatório, pois precisa descompactar o conainer
print(math.hypot(*p3d1))

# ESTATÌSTICA:

import statistics
# statistics.fmean - calcula a media de numeros reais
# statistics.geometric_mean - retorna a média geométrica
# statistics.multimode - retorna o valor mais frequente em uma sequencia


print(statistics.fmean([1.45, 43.3, 46.2, 4.5, 12.4]))

seq = [3, 5, 7, 8, 9]
seq2 = 'Geremias Correa'

print(statistics.multimode(seq))  # repete 1 vez cada
print(statistics.multimode(seq2)) # 'e' e 'r', repetem 3 vezes