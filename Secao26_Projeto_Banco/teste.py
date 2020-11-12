from models.cliente import Cliente
from models.conta import Conta


geremias: Cliente = Cliente('Geremias Corrêa', 'Geremias@gmail.com', \
    "123.456.789-43", "20/01/1997") 

gabriela: Cliente = Cliente('Gabriela Rebello', 'Gabriela@gmail.com', \
    "124.156.389-43", "27/09/1998")


print(geremias)
print(gabriela)

contaf: Conta = Conta(gabriela)
contaa: Conta = Conta(geremias)

print(contaf)
print(contaa)