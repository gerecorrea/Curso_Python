"""
Leitura de arquivos.

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open()

open() -> Na forma mais simples de utilização passamos apenas um parametro
    Que é o caminho do arquivo a ser lido.
    Assim ele será aberto para somente leitura

OBS: por padrão, a função open() abre o arquivo para leitura. Este arquivo deve
existir, ou então teremo FileNotFoundError

mode r -> modo de leitura. r -> read()

read() -> função extensiva da variável do arquivo aberto
    realiza a leitura do arquivo (de forma total!).
    Ex: arquivo.read()
    O retorno dele é em um formato de string que contém todo o conteúdo 
"""


# Exemplo

arquivo = open('arquivo.txt')
# print(arquivo)  # <_io.TextIOWrapper name='arquivo.txt' mode='r' encoding='UTF-8'>

print(arquivo.read())  # Realiza a leitura do arquivo.

# Obs: o Python utiliza um recurso para trabalhar com arquivos chamado cursor
# Ele funciona como um cursos quando estamos escrevendo, em que acompanha
# o texto.

# Após ler tudo, o curso do arquivo fica no final, por isso não dá para ler duas
# vezes
# print(arquivo.read())