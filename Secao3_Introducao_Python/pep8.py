# Dicas de padrão de código bem escrito do Pep8


"""

[1] - CamelCase para nome de classes.
class CalculadoraCientifica:
    pass  # pass para não fazer nada mas não gerar erro por falta de código

[2] - Utilize nomes em minusculo, separados por underline para funções ou
variáveis
def soma(a,b):
    return a+b

[3] - Utilize quatro espaços para identação! (obrigatório) - e não utilize
tabs, mas sim 'spaces', por conta de variação de configurações
if x:
    pass  # quatro espaços para escrita do pass abaixo

[4] - Linhas em branco:
    Duas linhas em branco antes de qualquer definição de classe
    Separar funções e definições com duas linhas em branco
    Métodos dentro de uma classe devem ser separados com uma única linha em
    branco

[5] - Imports devem ser feito sempre em linhas separadas, nunca na mesma linha
    Em caso de muitos imports de um mesmo pacote, recomendasse fazero "from
    pacote import
    (pacote1, pacote2, etc), sendo que cada pacote dentro do parentes estejam
    em uma linha,
    e o ')' numa outra linha extra

[6] - Espaços em expressões e instruções:
    Não colocar espaços após e antes '(' ou '{' ou '[' etc, assim como antes
    de fechá-los
    Deixar UM espaço antes e depois do sinal d '='

[7] - Termine sempre uma instrução com uma nova linha

[Extra] - Comentários à direita de código, com duplo espaço, então # e mais um
espaço antes da escrita

[Extra2] - Nomes dos scripts separados por por underline

[Extra3] - Um linha, em Python, deve conter, no máximo, 79 caracteres

[Extra4] - Sempre usar espaço antes de usar '+' da concatenação (como em print
de variáveis)

[Extra5] - Utilizar um linha extra em branco no fim de todo arquivo

"""
