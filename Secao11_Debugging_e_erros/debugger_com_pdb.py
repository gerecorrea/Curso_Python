"""
Debuggando com PDB

PDB -> Python Debugger

A utilização do print para debugg de código pode ser considerado uma prática
ruim

Utilizar o PyCharm ou o Python Debugger é considerado mais ideal
    Colocação de breakpoints no código (PyCharm)

Com o Python Debugger (PDB):
    Importar a biblioteca pdb
    Coloca um 'pdf.set_trace()' onde quer criar um 'breakpoint'
    Irá abrir um menu de execução, onde:
        digitar 'l' lista onde estamos no código (linha atual, não executada)
        digitar 'n' vai para próxima linha
        digitar 'p' imprime variaável
            Ex: p nome, imprime o nome
            Pode ser utilizado somente o nome da variável (caso não sejam l, n, p ou c)
        digitar 'c' continua a execução - finaliza o debugging
    Ele é bem manual, mas gostei, parece bom
    A partir do Python 3.7 pode se utilizar o breakpoint() e sem imports, mais efetivo

Pode ser declarado o import na linha de declaração do breakpoint do debugg
    Por que utilizar este formado (pdb)?
        É uma prática comum, fica opcional. Dado que faz o import de toda bib
        pode ser recomendado importar somente quando utilizar.
    Prefiro o método no início, mas bom, é uma opção

OBS: A partir do Python 3.7, não precisa mais fazer import do pdb
pode só chamar "breakpoint()" na linha que deseja debuggar
A tela de execução é a mesma do pdb.
"""

# Exemplo utilizando o Python Debugger

# import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
# pdb.set_trace()  # Seria como colocar um breakpoint aqui.
# import pdb; pdb.set_trace()  # Forma comum de utilização
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação 2'
final = nome_completo + ' faz o curso' + curso
print(final)
