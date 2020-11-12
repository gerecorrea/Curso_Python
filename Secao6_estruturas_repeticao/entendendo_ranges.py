"""

Ranges.

Conhecer o loop for para usar o ranges
Para trabalhar melhor com o for, o conhecimendo do range vem bem a calhar

Os ranges são utilizados para gerar sequências numéricas, aleatórias ou não

Forma geral: início 0 e passo 1 
range(valor de parada)  # o início padrão é 0 e passo de 1 em 1

Forma 2: Com início definido
range(valor_de_inicio, valor_de_parada)  # Inicio definido, passo de 1 em 1

Forma 3: Com passo diferente
for num in range (1, 10, 2):
    print (num)  # inicio e fim definido, com passo de 2 em 2

Forma 4: Forma inversa
for num in range(10, 0, -1): #vai de 10 a 0+1, de passo 1.
    print(num) 

"""

for num in range(10, 0, -1):  # vai de 10 a 0+1, de passo 1.
    print(num) 
