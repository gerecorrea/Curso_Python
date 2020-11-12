"""
Aplciando o GIL realmente, agora uso de mjutex para acessos

Demandam mais recursos e, consequentemente, são mais pesado que multithread
Mas melhora o desempenho

ELe utiliza o CPython como interpretador.
"""
from multiprocessing import Pool
import time

contador = 50000000


def contagem_regressiva(n: int) -> None:
    while n > 0:
        n -= 1


if __name__ == "__main__":
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [contador//2])
    pool.close()
    pool.join()
    fim = time.time()
    print(fim - inicio) # 1.3 segundos. E olha que esse caso nem é fantastico
    # pois o uso do mutex causa lentidão na execução, já que tem o time wait
