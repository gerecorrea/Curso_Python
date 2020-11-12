'''

Tipos numéricos

'''
var1 = 5
var2 = 2

# Dividindo por "/", retorna em float
print("Divisão padrão: ", var1/var2)

# Dividindo por "//" ele retorna o inteiro (se fizer o cast int(operacao) também funciona)
print("Divisão inteira: ", var1//var2)

# Operação de resto:
print("Resto: " +str(var1%var2))

#Potência
print("2^5: ", var2**var1)
print("2^1000: ", 2**1000)  # Repare que o Python não tem limite de casas.

# Incremento:
var2 += 1  # var2 + 1
var2 *= 3  # var2 * 3

#Tipo da variável
print("Tipo de var2: ", type(var2))

#Vendo as dir(num) no terminal, temos vários métodos, como?
print (var2)
var2.__add__(8)
print (var2)
