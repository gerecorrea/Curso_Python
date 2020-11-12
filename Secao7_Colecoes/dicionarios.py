"""

Dicionários.

Obs: Em algumas linguagens, os dicionários Python são conhecidos por mapas

Dicionários são coleções do tipo chave e valor.

É possível representá-los em listas e tuplas, através da replicação delas
    Representando então outros elementos em um mesmo índice

Importante lembrar que sempre é buscado pela chave, não pelo valor

Em dicionários temos que a forma de adicionar e atualizar é a mesma
    Com isso vemos que não podemos ter chaves repetidas
    Se não há, ele adiciona. Se há, ele atualiza

"""
# Forma 1 (mais comum e a indicada) para criação de dicionários:

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'es': 'Estônia'}
print(paises)

# Forma 2 (menos comum) para criação de dicionários:

# paises2 = dict(br='Brasil', eua='Estados Unidos', es='Estônia')
# print(paises2)

# Acessando elementos via chave (igual lista e tupla):

print(paises['br'])  # Imprime os valores através da chave
# print(paises['rus'])  # Gera erro (KeyError), pois a chave não existe

# Acessando elementos via get (forma recomendada):

print(paises.get('br'))  # retorna Brasil
print(paises.get('rus'))  # Não gera erro, mas sim retorna None (sem tipo)
# Tipo None é sempre considerado como False, caso use em um if, etc
# Definindo um valor padrão de retorno, para caso não encontre a chave
print(paises.get('ale', 'Não encontrado'))  # Caso não encontre, gera retorno

print("Brasil está incluso? R: ", 'br' in paises)

# Atribuindo elementos a variáveis especificas (off):
if 'br' in paises:
    brasil = paises['br']  # pega o valor brasil de países e add a variável
print(brasil)

# Podemos utilizar qualquer tipo de dado (int, float, string boolean):
# Inclusive lista, tupla dicionário, como chaves de dicionários.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (45.6895, 29.6917): 'Escritório em Nova Iorque',
    (55.6895, 19.6917): 'Escritório em São Paulo',
}

print(localidades)

# Adicionar um elemento em um dicionário

receita = {'jan': 100, 'fev': 200, 'mar': 150}
# Forma 1 (mais comum):
receita['abr'] = 225  # Adiciono no final uma chave abr com valor 225
# Forma 2:
novo_dado = {'mai': 200}
receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário (igual a adc):

receita['jan'] = 150  # Sobre escreve o valor de uma chave. Mais comum.
receita.update({'abr': 175})  # Outro forma. Menos comum.
print(receita)

# Remover dados de um dicionário:

receita.pop('fev')  # Remove o elemento de chave fev do dic. Forma 1
print(receita)
# Obs: lembrando que pop tbm retorna o elemento para uma variável, caso queira

del receita['mar']  # Remove o elemento mar do dic. Forma 2.
# Caso a chave não exista, retorna um KeyError
# Aqui não retorna o valor removido
print(receita)

# Imagine um contexto de comércio eletrônicos:
'''
    Carrinho de compras:
        Produto 1:
            - nome:
            - preco:
            - quantidade:
        ...
            ...
'''
# Por listas (mesmo pra tuplas):
carrinho = []
produto1 = ['Ps4', 2300.00, 1]
produto2 = ['Carro', 15000.00, 1]
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# O problema aqui é que preciso saber o indice de cada produto

# Por dicionário:
carrinho = []
produto1 = {'nome': 'Playstation', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'Carro', 'quantidade': 1, 'preco': 21000.00}
carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)
# Dessa forma facilmente adicionamos ou removes produtos no carrinho
# Além de ter a certeza sobre cada informação, buscando pela chave
print(carrinho[0])  # Retorna apenas o produto de pos 0, etc

# Métodos de dicionários:
# clear, copy, fromkeys, get, items, keys, pop, popitem, sedefault, update
# e values

receita = {'jan': 100, 'fev': 200, 'mar': 150}
print(receita)

# Clear
receita.clear()  # Limpa o dicionário completamente
print(receita)

# Copy
receita = {'jan': 100, 'fev': 200, 'mar': 150}
receita2 = receita.copy()  # Copia os dados para outro dicionário
receita3 = receita2  # Copia tbm, como não tem shallow copy, não gera problema
print(receita3)

# Criação de dicionários (de forma não usual) - BEM VÁLIDO
usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
# Neste método, nome, pontos, email e profile são todos chaves
# Enquanto o 'desconhecido' seria o valor
print(usuario)  # Printa o valor para cada chave
print(usuario['profile'])  # Print exemplo

veja = {}.fromkeys(range(1, 11), 'novo')  # Cria chaves de 0 a 10 com o valor
print(veja)
