"""

Ordered dict, do módulo Collections

"""

dicionario = {'a': 1, 'b': 2, 'c': 3}

for chave, valor in dicionario.items():
    print(f'chave {chave}; valor{valor}')
# Aqui manteve a ordem, mas isso não é garantido, para isso se tem o Ordered

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3})

# Diferença entre dict e ordered dict:

# Dicionário comum
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 2, 'a': 1}
print(dic1 == dic2)  # Retorna True, pq aqui a ordem não importa

# Ordered Dict
order_dic1 = OrderedDict({'a': 1, 'b': 2})
order_dic2 = OrderedDict({'b': 2, 'a': 1})

print(order_dic1 == order_dic2)  # Retorna false, pq nele a ordem importa