"""
Como funciona a alocação e gerenciameto de memória em Python

Tem uma ideia interessante, diferente de C, por exemplo

Nela, ao atribuir uma variável ao um valor, dado tipo aponta para um local alo-
cado na memória.
-Quando outro objeto recebe a atribução da primeira variável, não é criado uma 
nova alocação, mas sim ambas varia´veis apontam para a mesma posição na mem
-Caso uma das variáveis receba um novo valor, então o Python aloca uma nova
memória para a variável com novo valor apontar para ela
-Caso seja criada uma variavel = valorqlqr, se o valor já feve memória alocada,
essa memória é reutilizada para a nova variável apontar para ele.
    Mesma lógica funciona para um objeto do tipo classe ou outra.

A alocação da memória é feito primeiramente na memória stack, que aponta para
a alocação realizada na memória heap.
    Na stack fica o main, funcaoX() etc, mas não as alocações das variáveis em si

O algoritmo utilizado pelo Garbage Collector é o Reference Couting
    Por padrão é o Python escrito em C (o CPython), apesar de tbm existir o PyPy,
etc. 

Comparação entre as lingaugens:
- O que é 10? Para python, é um objeto criado na memória heap, enquanto em C é um
dado primitivo de 2 bytes.
- O que x contém? refrencia o Objeto 10, enquanto em C é o local de memória onde
10 está armazenado
- quando muda para 11? Em C mantemos a alocação, mudamos seu valor (problema do
efeito cascata), euqnato em Python ele cria uma nova alocação.
    Vantagens e desvantagens de cada.


"""