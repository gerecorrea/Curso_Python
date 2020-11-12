"""

Deque, do módulo Collections.

O Deque é basicamente uma lista de alta performance



"""

from collections import deque

# Criando deques:

deq = deque('geek')
print(deq)  # cada letra para uma posição

# Adicionando elementos no deque

deq.append('y')  # Adiciona no final, padrão
print(deq)

deq.appendleft('k')  # Adiciona na primeira posição
print(deq)

# Remover elementos:

deq.pop()  # remove o ultimo
print(deq)
deq.popleft()  # Remove o primeiro
print(deq)