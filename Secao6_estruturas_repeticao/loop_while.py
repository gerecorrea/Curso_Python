"""

Laço while.

Forma geral (como exemplo 1 e 2):
while expressão_booleana:
    //Execução do loop


Forma 2:


"""
# Exemplo 1:
num = 10
while num > 0:
    print(num)
    num -= 1

# Exemplo 2:
resposta = ''
while resposta != 'sim': # Em while aceita == e !=, mas não is ou is not, ou not
    resposta = input("Já acabou, Jéssica? R: ")