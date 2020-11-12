"""
Sistemas de arquivos - manipulação

Nesta aula foi visto como verificar se um diretório existe
Como abrir um diretório
Como criar um diretório e multi-diretórios
Como renomear arquivos
Como deletar arquivos
"""

import os

# Descobrindo se um arquivo ou diretório existe:
print(os.path.exists('frutas.txt'))
print(os.path.exists('frutas'))

# Em paths absolutos:
print(os.path.exists('/home/geek/Imagens'))

# Criando arquivos - Forma 1:
# open('arquivo-teste.txt','w').close()

# with open('arquivo-teste2', 'w') as arquivo:
    # pass

# Criando arquivos - Forma 2 - ideal:
# os.mknod('arquivo-teste3.txt')  # Cria um arquivo no dir atual
# os.mknod('/usr/arquivo-teste3.txt')  # Cria um arquivo no dir especificado
# Se já existir, retorna FileExistirError

# Criando diretórios um a um - da forma ideal:
# os.mkdir('templates')  # Cria o diretório template
# Obs: Se já existir, retorna FileExistirError

# Criando multi-diretórios (vários por vez):
# os.makedirs('templates/geek/university')
# pode passar um paraemtro extra que exclui o aviso do erro (exist_ok=True)

# Renomear um arquivo ou diretório:
# os.rename('template2', 'geek2')  # Renomeia o tempalte2 para geek2
# Caso faça para multi-diretório, o caminho todo precisa ser igual mesmo assim
# Apenas muda o nome do arquivo final em si

# Deletar arquivos (somente para arquivos mesmo):
# Obs: cuidado, ao deletá-los por aqui os deletam eternamente
# os.remove('geek.txt')  # Removendo o arquivo geek.txt
# No Windows, se for deletar e estiver aberto, retorna erro.
# send2trash('cesta2.txt')  # Envia para a lixeira, lib externa pelo pip install
# T

# Deletar diretórios (somente para dirs) sem nada dentro:
# os.rmdir('templates')  # Remove somente diretórios vazios
# os.removeidrs('geek2/deee')  # Remove todos eles, mas somente se estão vazios

# Deletar diretório e recursivamente tudo que tem dentro (talvez só arquivos):
"""for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)"""

# Trabalhando com arquivos e diretórios temporários:

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f"Criei o diretório temporário em {tmp}")
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek university\n')
    input()
# Após a saída do with, após sair dele tudo é excluído
# Em arquivos temporários só conseguimos escrever bits, por isso 'geek' vira
# b'geek', etc.