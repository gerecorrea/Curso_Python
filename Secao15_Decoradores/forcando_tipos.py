"""
Forçando tipos de dados com decoradores.

Vamos ter uma aplicação prática do mesmo
    Mas com o objetivo de forçar os tipos de dados com os decoradores

"""

from typing import List


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)  # str para msg, int para vezes
def repeat_msg(msg: str, vezes: int):
    """Repete dada msg x vezes."""
    for _ in range(vezes):
        print(msg)

repeat_msg('Hey hey, you you', 5)


@forca_tipo(float, float)
def dividir(a: float, b: float) -> float:
    return a / b


print(dividir(3, 5.2))
