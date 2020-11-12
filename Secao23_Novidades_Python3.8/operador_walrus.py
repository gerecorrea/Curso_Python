"""
Operador Walrus.

O operador Walrus permite fazer a atribuição e retorno em uma única expressão
    Apenas para garantir maior patricidade, não há nada novo

Sintaxe:

variavel := expressão

Obs: precisa estar utilizando Python3.8+ para tal (atual 3.8.2)

Quando você deve ou não usar este oepraodr:
    Quando você quiser, desde você conhece o recurso e achar necessário utiliz.

"""

# Exemplos de uso (direto, sem mostrar o padrão no python pq é óbvio):

print(nome := 'Geremias Correa')

cesta = []
while (fruta := input("Informe a fruta: ")) != 'jaca':
    cesta.append(fruta)
print(cesta)