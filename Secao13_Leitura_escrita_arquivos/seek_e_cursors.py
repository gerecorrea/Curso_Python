"""
Seek e Cursors

seek() -> é utilizado para movimentar o cursor pelo arquivo

close() -> Função para fechar a conexão do script com o arquivo no disco do pc
    É uma função extensiva do arquivo aberto, acesso via, ex, arquivo.close() 
"""

arquivo = open('arquivo.txt')

print(arquivo.read())

# Lendo o aruqivo novamente movimentando o cursor para o começo

arquivo.seek(0)  # Joga o cursor para primeira posição do arquivo, para poder
# lê-lo novamente.

print(arquivo.read())

# Lendo uma única linha:

arquivo.seek(0)

print(arquivo.readline())  # Lê somente uma linha, a atual do cursor
print(arquivo.readline())  # Lê a segunda linha do arquivo, dada a posição do c.
# Obs: repare que o readline pula linha ao final da leitura por conta do print
# basta modificar o parametro end da função

# LEndo toda as linhas e colocando em uma lista de string (para cada linha):

arquivo.seek(0)

lista_linhas = arquivo.readlines()  # Lê todas as linhas e cada linha vira uma string
# de uma dada lista
print(f"Quantidade de linhas: {len(lista_linhas)}")


# Para ler uma quantidade de caracteres específica:
arquivo.seek(0)
print(arquivo.read(10))  # Lê os primeiros 10 caracteres

# Obs: quando abrimos um arquivo é criada uma conexao entre o arquivo no disco
# do cmputador e o script. Então, ao finalizar a execução do trabalho, deve
# se fechar a conexão, por boa prática e segurança


# Fehca o arquivo
arquivo.close()

# Verificar se o arquivo está aberto ou fechado:

print(arquivo.closed)  # verifica se arquivo está fechado

