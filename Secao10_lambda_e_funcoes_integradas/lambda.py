"""Funções lambda.

Expressões lambda são expressões/funções sem nome, ou seja, anonimas
    São basicamente funções inline (se aproxima do arrow function do js)

Muito úteis para filtragem e ordenação de dados (mas não só isso)
"""

numeros = [1, 2, 3, 4, 5]

# Expressãõ lambda:

calc = lambda x: 3 * x + 1
# lambda é apenas o nome para indicar que é uma função sem nome
print(calc(4))

# Faz o mesmo que:
# def funcao(x):
#     return 3 * x + 1

# Podemos usar expressões lambda com múltiplas entradas:

nome_completo = key=lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('    Geremias  ', '    Corrêa'))
# Strip() remove espaços no ínicio e final da variável/string
# Pode usar o "key=", é opcional

# Podemos ter nenhuma ou várias entradas
amar = key=lambda: 'Como não amar python'
print(amar())

tres = lambda x, y, z: x * y + z
print(tres(3, 5, 6))
# Obs: se passarmos mais argumento que o esperado, teremos TypeError

# Outro exemplo:

autores = ['J. R. R. Tolkien', 'Stephen King', 'H. G. Wells']
print(autores)
# Vamos ordenar por sobrenome, inclusive:
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
# Obs: [-1] pega o último elemento de uma lista, que é identificado pela
# separação entre espaços


# Exemplo 3 - Definindo função quadrática em python com lambda:
def geradora_funcao_quadratica(a: int, b: int, c: int) -> int:
    """Retorna f(x): ..."""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)  # a, b, c

print(teste(0))  # passa variável x do lambda
print(teste(1))
print(teste(2))

# Ou:
print(geradora_funcao_quadratica(2, 3, -5)(2))
