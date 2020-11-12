"""Erros mais comuns em Python.

É importante entender e ler a saída de erros e interpretar corretamente
    Ela auxilia muito a identificar o erro que está acontecendo
O gerador de erros do Python faz um traceback dos passos executados até o erro
    Bastante efetivo partindo da interpretação do programador

Erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe.
    a)  def funcao:
            print('Geek university)
    b)  def = 1
    c)  return

2 - NameError -> Ocorre quando uma variável ou função não foi definida
    a)  print(geek)  
    b)  geek()

3 - TypeError -> Ocorre quando uma função/ação é aplicada a um tipo errado
    a)  print(len(5))
    b)  print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou
outro tipo de dado utilizando um índice inválido.
    a)  lista = ['Geek']
        print(lista[0][10])  # Posição não existe

5 - ValueError -> Ocorre quando uma função ou operação built-in recebe um
argumento com um tipo correto mas valor inapropriado
    a)  print(int('Geek'))

6 - KeyError -> Ocorre quando tnetamos acessar um dicionário com uma chave
que não existe
    a)  dic = {}
        print(dic['geek'])  # o dic é vazio, logo não existe tal chave

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função
    a)  tupla = (11, 2, 31, 4)
        print(tupla.sort())  # sort() não existe para tuplas.

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python
    a)  def nova():
        print ('Geek')  # Faltaram os quatro espaços

OBS: Exceptions e erros são sinônimos na programação

"""

