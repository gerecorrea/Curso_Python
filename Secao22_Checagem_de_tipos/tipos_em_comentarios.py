"""


"""

import math


def circunferencia(raio):
    # type: (float) -> float
    """Da seguinte forma também é aceitável fazer o type hinting.
        Se fizer uso, colocar o docstring após ele.
    Mas não é permitido utilizar os dois, ou um ou outro.
    Apesar disso é mais recomendável o type hinting padrão."""
    return 2 * math.pi * raio


def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    return 'b'



if __name__ == "__main__":
    print(circunferencia(5))