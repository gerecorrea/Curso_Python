"""
Teste de velocidade com Expressões Geradoras.


"""
import time

# Generators (Geradores) - escrevendo um gerador:
def nums():
    """Escrevendo o gerador."""
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # Generator

print(next(ge1))
print(next(ge1))

# Generator Expression:
ge2 = (num for num in range(1, 10))
print(next(ge2))
print(next(ge2))

print(sum(num for num in range(1, 10)))  # 1 + 2 + 3 + ... + 10

# Teste de veloccidade com generator expression:
gen_inicio = time.time()
print(sum(num for num in range(1, 10000000)))  # 0.875 s
gen_tempo = time.time() - gen_inicio

# Teste de veloccidade com List Comprehension:
list_inicio = time.time()
print(sum([num for num in range(1, 10000000)]))  # 1.281 s
list_tempo = time.time() - list_inicio

print(f"Generator expression levou {gen_tempo}")
print(f"List Comprehension levou {list_tempo}")

# Com isso pudemos ver que generator expression é um pouco mais rápido
# Porém estamos usando Python, se quisessemos velocidade não optaríamos por ela
