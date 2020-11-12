"""
Sistemas de arquivos - navegação.

POdemos criar, editar também arquivos e diretórios de dentro do Python
    Variando suas extensões e etc, assim como outras linguagens.

Nos diretórios, temos estruturas hierárquicas (funcionamento em árvore)
    sudo apt-get install tree (apenas para ver a disposição)
No windows temos o diretório raíz 'C:\' e no POSIX o '/' (que é melhor)

$ pwd  # caminho completo do arquivo em relação ao raíz
    path abosuluto: raíz ao arquivo
    path relativo: quando não importa o que tem depois de x arquivo/diretório
        ex: $ /home/geek/Imagens/../

Quando se abre o console do Python, caso se abra ele na pasta correto com dados
arquivos, então temos os arquivo a disposição em mãos (sem navegação extra)

"""

import os

# Pega o diretório/path atual de trabalho.
print(os.getcwd())
print(os.path.dirname(os.path.abspath(__file__)))

# Para mudar o diretório: chdir()
os.chdir('..')  # Vai voltar um diretório
print(os.getcwd())

# Voltando ao diretório Secao13: 
res = os.path.join(os.getcwd(), 'Secao13_Leitura_escrita_arquivos')
os.chdir(res)
print(os.getcwd())

# Checar se um diretório é absoluto (true) ou relativo (false):
print(os.path.isabs('/home/gerecorrea/'))

# Se for usuário Windows:
print(os.path.isabs('C:\\Users\\gerecorrea'))  # Com caractere de escape

# Podemos identificar o sistema operacional com o módulo os (operate system)
print (os.name)  # Saída: posix, dado que é Linux
print(os.uname())  # mesmo do comando "uname" no terminal

# Juntando diretório com algo:
# res = os.path.join(os.getcwd(), 'novoDir')  # Concatena elementos pro diret.
# os.chdir(res)  # Vai ao novo diretório

# Print diretórios e quantidade:
print(os.listdir('/etc'))  # Printa os diretórios dentro do diretório etc.
print(len(os.listdir('/etc')))  # Printa a quantidade de diretórios
print(list(os.scandir('/etc')))  # Retorna o tipo de cada um dos objetos contid.

# Operações booleanas com diretórios:
arquivos = list(os.scandir())
print(arquivos[0].inode)  # ??
print(arquivos[0].is_dir)  # É um diretório?
print(arquivos[0].is_file)  # É uma arquivo
print(arquivos[0].is_symlink)  # É um link simbólico
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat)  # Informações estatísticas


# Abaixo anotações rapidinho de coisas úteis pro chamado talvez:

# Com o os.path.join

# os.makedirs ('nomeDiretório)  # cria diretório dentro do caminho atual
# Com tratamento de erro FileExistsError: Files exists: 'name'
# Existe um segundo parametro opcional "exists_ok = True" para impedir o erro.
# os.makedirs("dir1/dir2")  # cria um subdiretório dentro de um diretório

# Verificando a existência de um caminho e criando, caso não exista:
# if not os.path.exists('name'):
#    os.makedirs('name')

# Para criar um caminho com path join:
# mypath = os.path.join('dir1', 'dir2', 'dir3')  # Cria diretórios encadeados
# A vantagem acredito ser se adaptar ao tipo de escrita do SO em questão 

# Ideia, o usuário lança os usuários requisitados pelo cmd