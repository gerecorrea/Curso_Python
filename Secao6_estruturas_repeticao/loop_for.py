"""

Loop for (repetição).

Loop é uma ideia de estrutura de repetição

O for é uma dessas estruturas

Em Python:
for item in interval:
    loop

Exemplos de iteráveis: strings, listas, range (objeto).
"""

# Obs: Caso não queira que pule uma linha no print:
# print(conteudo, end='')


def run():

    nome = 'Geek University Code School'
    lista = [1, 3, 5, 7, 9]

    # Iterando sobre o range:
    for i in range(0, 10):
        print(i)
    # Sobre o range:
        # O valor final não é "inclusive", vai até o limite - 1
        # O valor inicial é opcional
            # Caso não coloque, como em range(10), vai começar em 0
        # Caso o valor iterado ultrapasse o limite, ele simplesmente não pega,
        # não dá seg fault, por exemplo

    print()

    # Iterando sobre uma string:
    for letra in nome:
        print(letra, end='')
    print()

    # Iterando sobre uma lista:
    for numero in lista:
        print(numero, end='')

    # Encontrando caractere enumerate:
    # Vai criar uma lista de tuplas do tipo: ((0, 'G'), (1, 'e'), ...)
    print()
    for indice, letra in enumerate(nome):
        print(f'Letra {letra} encontrada na posição {indice}.')  # Forma legal de print
        # print("Letra " + letra + " encontrada na posição " + str(indice))  # Forma mais padrão

    print(nome*5)  # Printa a mesma string 5 vezes.

    # Emojis:
    # Para mostrar um emoji, pegue o unicode dele e substitua o "+" por "000"
    # Nesse caso peguei o sorriso, que é U+1F600. Troquei pelo ice ball U+F300
    # Fiz uma seta de emoji pra cima (diferente do vídeo)
    for num in range(1, 20):
        for num2 in range (num, 10):
            print(" ", end='')
        if(num <= 10):
            print('\U0001F300' * num)
        else:
            print('     ' + '\U0001F300' * 5)


if __name__ == "__main__":
    run()