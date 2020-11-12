"""
Demonstrando o uso do GIL

"""
import time


contador = 50000000


def contagem_regressiva(n: int) -> None:
    """Função single-thread exemplo."""
    while n > 0:
        n -= 1

inicio = time.time()
contagem_regressiva(contador)
fim = time.time()

print(fim - inicio, " segundos.")  # 3.1 segundos