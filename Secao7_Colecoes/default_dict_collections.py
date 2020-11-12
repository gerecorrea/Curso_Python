"""

Default dict, do módulo Collections

São dicionários com todas as funções que conhecemos/vimos (e extras)

Mas possui algumas diferenças:
    Não gera o KeyError caso não ache a chave

Default Dict -> Ao criar um dicionário utilizando-o, n´os informamos um valor
default, podendo utilziar um lambda para isso. Este valor será utilizado
sempre que não houver um valor definido. Caso tentemos acessar uma chave que
não existe, essa chave será criada e o valor default será atribuído

Obs: lambdas são funções sem nome que podem ou não receber parâmetros de
entrada e retornar valores. Terá uma seção específica para isso ainda.

"""

# Import
from collections import defaultdict

dicionario = {'curso': 'Programação em Python: Essencial'}
print(dicionario)
print(dicionario['curso'])

dicionario2 = defaultdict(lambda: 0)

dicionario2['curso'] = 'Programação no que quiser'

print(dicionario2['curso'])
print(dicionario2['outro'])
# Como 'outro' não existe, ele cria, adiciona e dá valor default(0) a ele

