"""
Escrevendo em arquivos

Obs: ao abrir um arquivo para leitura, só podemos lê-lo, não escrever nele

para escrever num arquivo, precisamos abrir com 'w', para escrita, como segundo
parametro, que no caso é opcional
    Além da utilizaçao da função write()

write() -> Função apra escrita em arquivos.

"""

with open("arquivo_teste.txt", 'w') as arquivo:
    arquivo.write("Escrevendo neste arquivo.\n")
    arquivo.write("Blind Guardian é top.\n")
    arquivo.write("Stratovarius também!\n")

# Repare que quando você abre uma rquivo para escrita, na abertura ele exclui
# tudo que tinha no arquivo anteriormente.

# forma não pythonica de escrever em arquivos (como em c, por ex):

with open('arquivo.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta: ')
        if fruta != 'sair':
            arquivo.write(fruta + "\n")
        else:
            break