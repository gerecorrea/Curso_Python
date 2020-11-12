""" len(), abs(), sum(), round().

Funções simples básicas e inerentes da linguagem

len() -> retorna a qtd de itens de um iterável

abs() -> retorna o valor absoluto d um iterável, qlqr numérico

sum() -> retorna a soma dos elementos de um iterável
    Todos os elementos precisam ser numéricos
    INclusive o valor inicial (por default 0), que seria o segundo parametro

round() -> arredonda as casas decimais do vaor
    Precisa ser valor real
    São dois parametros, primeiro é o valor, segundo a qtd de casas
    Ele arredonda, não trunca. Se acima de .500000 arred para cima

"""

# len():
print(len((1, 2, 3, 4, 5, 6, 7, 8)))

# por debaixo dos panos o len() faz
# __len__(), chamada de "Dunder len" (Dunde pois usa __) 

print([1, 2, 3, 4].__len__())

# abs():
print(abs(-3.51))

# sum():

print(sum([1, 2, 3, 4, 5], 5))  # Soma todos,inclusive o valor inicial/default

# round():

print(round(3.1256752752, 5))  # pega 5 casas decimais (pós-vírgula)
print(round(17823618726328))  # Arredonda para um inteiro, nesse caso
