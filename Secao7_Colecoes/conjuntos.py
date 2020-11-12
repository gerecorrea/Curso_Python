"""

Conjuntos.

Se refere a teoria dos conjuntos da matemática (geral)

No Python, os conjuntos não chamados de "Sets"

Dito isto: 
    Sets (conjuntos) não possuem valores duplicados
    Sets não possuem valores ordenados
    Elementos não são acessados via índice, ou seja, conjuntos não são indexad

Conjuntos são bons para se utilizar quanto precisamos armazenar elementos,
mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados

Os Sets são referenciados em Python com chaves {}

Diferença entre Sets (conjuntos) e Mapas (dicionários):
    Um dicionário tem chave valor
    Enquanto um conjunto tem apenas valor

Nele pode conter quaisquer tipos de dados em um mes set, como int, string, etc

Conjuntos são bem válidos para uso na ciência de dados e IA
    Assim como a linguagem de forma geral


"""

# Definindo um conjunto:

# Forma 1 (menos comum)
s = set({1, 2, 3, 5, 6, 8, 11, 3, 5}) 
print(type(s))
print(s)
# Obs: repare que ele ignora os valores repetidos do conjunto

# Forma 2 (mais comum)
s = {1, 2, 3, 4, 5, 2, 8, 12, 15}
print(s)

if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Importante lemrar que também não se tem ordem:
lista = [99, 2, 12, 1, 2]
tupla = (99, 2, 12, 1, 2)
dicionario = {}.fromkeys(lista, 'dict')
conjunto = {99, 2, 12, 1, 2}
print(f'Lista: {lista}')  # Retorna 5 elementos
print(f'Tupla: {tupla}')  # Retorna 5 elementos
print(f'Dici.: {dicionario}')  # Retorna 4 elementos
print(f'Conj.: {conjunto}')  # Retorna 4 elementos, numa ordem que ele que faz

# Usos interessantes com sets:

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira
# ou museus e os visitantes infroamm manualmente a cidade de onde vieram
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista
# adicionar novos elementos e ter repetição

cidades = ['BH', 'SP', 'Campo Grande', 'Cuiabá', 'SP', 'Cuiabá', 'PA']

# Precisamos saber quantas cidades distintas foram visitadas, então entrao set
print("Cidades visitadas: ", len(set(cidades)))  # Com o set, retira repet.

# Adicionando elementos em um conjunto:

s = {1, 2, 3}
s.add(4)  # Forma padrão de adicionar um elemento a um conjunto
print(s)

# Removendo elementos em um conjunto:

s.remove(3)  # Remove o valor 3. Forma 1 de remoção
print(s)

s.discard(2)  # Remove o valor 2. Forma 2 de remoção
print(s)

# A diferença entre eles, é que no discard, caso não haja valor, não gera erro
# Ambos não geram retorno ao excluir um elemento

# Copiando um conjunto para outro:

s = {1, 2, 3}
print(s)
s2 = s.copy()  # Deep copy, forma 1, não modifica o primeiro
s3 = s  # Shallow copy, forma 2, modifica o conjunto s também! 
print(s2)
print(s3)
s2.add(4)
s3.add(4)
print(s)
print(s2)
print(s3)

# Remoção de todos os elementos de um conjunti:

s.clear()
print(s)

# Métodos matemáticos de conjuntos:

# Imagine dois cursos, um alunos do curso de Python e outro do de Java
estudantes_python = {'Rodrigo', 'Maria', 'Gabriela', 'Júlia'}
estudantes_java = {'Fernando', 'Priscila', 'Gabriela', 'Rodrigo'}
# Veja que há interseção de alunos que estudam ambos os cursos

# Union (União entre dois conjuntos)
estudantes_totais = estudantes_python.union(estudantes_java)  # Forma 1
print(estudantes_totais)
estudantes_totais = estudantes_python | estudantes_java  # Forma 2
print(estudantes_totais)
# Obs: repare que usando "+" não é aceito em conjuntos/set
# O union é mais recomendado, pois é mais claro

# Intersection (Interseção entre dois conjuntos):
estudantes_de_ambos = estudantes_python.intersection(estudantes_java)  # Forma1
print(estudantes_de_ambos)
estudantes_de_ambos = estudantes_python & estudantes_java  # Forma2
print(estudantes_de_ambos)
# Obs: novamente, uso do intersection pe mais indicado

# Outter/Difference:
estudante_so_de_python = estudantes_python.difference(estudantes_java) # Form1
print(estudante_so_de_python)
# Obs: repare que aqui retira os repetidos, deixa somente os únicos

# Soma, max, min, tamanho (se todos numéricos):
s = {11, 22, 3, 4, 5, 6, 7}
print("Sum s:", sum(s))
print("Max s:", max(s))
print("Min s:", min(s))
print("Tam s:", len(s))
