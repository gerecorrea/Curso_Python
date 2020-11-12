"""
Demonstrando o GIL. Multithread.


"""
import time
from threading import Thread

contador = 50000000


def contagem_regressiva(n: int) -> None:
    while n > 0:
        n -= 1

t1 = Thread(target=contagem_regressiva, args=(contador//2,))
t2 = Thread(target=contagem_regressiva, args=(contador//2,))

inicio = time.time()
t1.start() # aloca
t2.start()
t1.join() # inicia e executa realmente
t2.join()
fim = time.time()
print(fim - inicio)  # 3.45 segundos (vai ser algo próximo do single_thread)

# O desempenho é completamente afetado pois temos uas threads acessando e modi-
# ficando a variável ao mesmo tempo. IMplica tanto em resultados errôneos quanto
# pouca melhora de código.
# Em diversos casos também pode causar deadlock.