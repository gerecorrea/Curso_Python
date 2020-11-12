"""

Breaks.

Funciona igual ao C, etc.

Utiliza o break para sair de loops de maneira projetada

"""

for numero in range(1, 11):
    if numero == 6:
        print(numero, "last time :/ ")
        break
    else:
        print(numero)

while True:
    comando = input("Digite 'sair' para sair.")
    if comando == 'sair':
        break
