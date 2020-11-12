"""

Funções com parâmetro.

São funções que recebem dados para serem processados dentro da mesma

Caso seja somente um parâmetro, basta colocar dentro das ()
    Caso tenha mais de um, devem ser separados por vírgula
    Parâmetros são as variáveis declaradas na definição de uma função
    Argumentos são os dados passados durante a execução da função
    É questão de nomenclatura, são as mesma coisa mas em momentos diferentes

Funções podem ser divididas (e veremos nessa aula):
    Com entrada e ocm saída
    Com entrada e sem saída
    Sem entrada e com saída
    Sem entrada e sem saída

"""
# Obs: to colocando o retorno "-> tipo" em alguns, mas não precisa
# O mesmo para o __main__ que to fazendo mas no vídeo não

# Para retorno de lista na função
from typing import List


def quadrado(numero: int) -> int:
    """Docstring."""
    return numero*numero


def cantar_parabens(aniversariante: str) -> None:
    """Docstring."""
    print(f"Parabéns para você, {aniversariante}")


def soma_tripla(a: int, b: int, c: int) -> int:
    """Docstring."""
    return a+b+c


def batman_nan(quantidade: int, msg: str) -> None:
    """Docstring."""
    for _ in range(quantidade):
        print(msg, end=' ')
    print()
    # Deixei "_" pois não utilizo o índice


def lista_tam_var(tamanho: int) -> List[int]:
    """Docstring. Não entendi o erro."""
    lista = list(range(tamanho))
    return lista


if __name__ == "__main__":
    print(quadrado(5))  # printa o quadrado de 5

    cantar_parabens("Rodrigo")

    print(soma_tripla(2, 6, 10))

    batman_nan(5, 'NaN')

    batman_nan(msg='DiNg DInG', quantidade=4)  # caso queira passar em outra ordem

    print(lista_tam_var(50))
