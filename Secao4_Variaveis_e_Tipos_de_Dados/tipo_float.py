'''

Tipos numéricos do tipo float
    Numérico do tipo real/decimal, então que contpem casas decimais

'''
var2 = 1,44  # Entende como sendo uma tupla
print (var2)

var1 = 1.44  # Entende como sendo um flaot realmente.
print (var1)

# Dupla atribuição de tipos:
var3, var4 = 1.44, 1.66
print ("var 3 e var4: ", var3, var4)

# Float to int:
var3 = int(var3) # Ele trunca o valor, não arredonda, então perde precisão
print("var3 int: ", var3)

# Int to float:
var3 = float(var3)
print("var3 float: ", var3)

# Tipos complexos:
complexo = 5j  # Com o 'j' no final entende como complexo
print("Complexo:", complexo)

