"""
Assertions (Checagens):

Em Python utilizamos a palavra reserva "assert" para realizar simples
afirmações utilizadas nos testes.
    Apesar disso, try except é mais recomendado. Talvez para testes específicos
    o assert pode vir a ser mais útil.

A ideia é utilizar o assert como xpressão para checagem se válida ou não
    Se a expressão vor verdadeira, o assert levanta "None", caso contrário,
    retorna AssertionError

# OBS: Nós podemos especificar, opcionalmente, um segundoa rugmento ou mesmo
mensagem de erro personalizada

# OBS: a palavra assert pode ser utilizada em qualquer função ou código nosso
    Sem ser necessariamente um caso de teste

# CUIDADO AO UTILIZAR ASSERT:
    Se um programa for executado com a flag -O, nenhum assertion será válidado
        Seria por conta de ser uma flag de otimização e o assert acaba sendo
        ignorado?
        De qualquer forma, dá pau na execução do código.
    A utilização do try except é o jeito mais correto.

"""


def soma_num_pos(a: int, b: int) -> int:
    assert a > 0 and b > 0, 'Ambos números precisam ser positivos'
    return a + b


def run(comida: str) -> str:
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita'
    ], 'A comida precisa ser fast food'
    return f"Estou comendo {comida}"


print(soma_num_pos(2, 4))  # ok
# print(soma_num_pos(2,-4))  # erro avisado.
print(run('pizza'))

