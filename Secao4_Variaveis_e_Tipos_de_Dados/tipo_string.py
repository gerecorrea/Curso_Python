'''

Tipo string

São cadeias de caracteres

É considerado desse tipo sempre que:
    Estiver entre aspas simples ou duplas
    Estiver entre aspas simples triplas ou duplas triplas
'''

var = "string exemplo"
print("String exemplo: " + var)

var2 = '''ex'''
print(var2)

# Quando se tem uma string com aspa simples, se usa ela envolvida em aspas
# duplas, por ex:
var5 = "Pub's Bar"

# Converter de outro para string:
var3 = 4
var4 = str(var3)

# Converter de string para outro tipo:
var6 = int(var4)
var7 = float(var4)

# Converter tamanhos:
nome = "geremias"
nome.upper()  # Tudo maiúsculo 
nome.lower()  # Tudo minúsculo
nome.title()  # Apenas as iniciais de cada string da variável maiúsculas

# Split:
# ['G','e','e','k',' ','U', ... ,'l']
nome = "Geek University Code School"
print(nome[0:4])  # printa de 0 a 3 a variável a nome. Chamado de string slice
print(nome[::-1])  # Pega da primeira posição até a última e inverte
print(nome.split())  # Printa a lista separando as strings por espaço
print(nome.split(' '))  # Faz o mesmo da linha anterior.
print(nome.split()[1])  # Acessa a segunda palavra da lista, no caso university
print(nome.replace('e', 'i'))  # Troca todas as aparições da letra 'e' por 'i'

# Ver mais métodos em dir("string")
