'''

Tipo Booleano, lá do George Boole

2 constantes: True e False
Obs: sempre como inicial maiúscula

'''

var1 = True
var2 = False

# Padrão:
print (var1)

# Negação:
print(not var1)

# Or (operação binária):
print (var1 or var2)  # Se um é verdadeiro, retorna True. Só retorna falso se ambos False

# And (operação binária):
print (var1 and var2)  # Retorna verdadeiro se todos são verdadeiros. Caso contrário, retorna False

#Exemplo de condicional usando os bool e as operações
if var1 == True and var2 == True:
    print("Full ativo")
elif var1 == True or var2 == True:
    print("Semi-ativo")
else:
    print ("Desativado")

#Retorno booleanos pelo print:
print (5>6)
print (2**4 < 14)
print (65 == 5 * 13 or 123 == 234//2)