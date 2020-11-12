"""
List Comprehension parte 2.

Podemos adicionar estruturas condicionais lógicas às nossas listas


"""

# Exemplo 1:

numeros = list(range(100))

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando:
pares_2 = [numero for numero in numeros if not numero % 2]
impares_2 = [numero for numero in numeros if numero % 2]
# Obs: isso ocorre porque 1 é True, 0 é False, o que for True ele add.
print(pares_2)
print(impares_2)

# Exemplo 2:
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
# Obs: Neste, se par ele multiplica por 2, se impar ele divide por 2