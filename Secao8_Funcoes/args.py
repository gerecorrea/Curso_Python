"""
Entendendo o *args

É um parâmetro, como outro qualquer
Isso significad chamar de qlqr coisa, desde que comece com *

Exemplo:

*xis

Mas, por convenção, foi adotado o nome "*args" para defini-lo

Ele coloca os valores extras informados como entrada em uma TUPLA
    Lembrando que tuplas são imutáveis
É mais útil que precisar ficar adaptando a função a quantidade dos parametros
chamados.

Para declarar nomeamos *args, para utilizá-lo apenas args
"""

# Exemplo 1 de utilização


def soma_todos_numeros(*args: int) -> int:
    """Função que soma todos os números."""
    """ Jeito ruim:
    total = 0
    for numero in args:
        total += numero
    return total
    """
    return sum(args)


def verifica_info(*args: str) -> str:
    """Verifica se os dados passados são válidos."""
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo, Geek'
    return 'Eu não lembro quem você é!'


if __name__ == "__main__":
    print(soma_todos_numeros(1))
    print(soma_todos_numeros(1, 2))
    print(soma_todos_numeros(1, 2, 3))
    print(soma_todos_numeros(1, 2, 3, 4)) 

    print(verifica_info('Geek', 'University'))
    print(verifica_info('Geek', 'Pão'))

