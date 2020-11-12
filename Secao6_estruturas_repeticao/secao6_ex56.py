"""

Exercícios da seção 6 - exercício 56

Triângulo de Floyd

"""
def run():
    linhas = input("Digite um número: ")
    contador_numero = 0

    for contador_linhas in range(0, int(linhas)):
        for n2 in range(0, contador_linhas+1):
            contador_numero += 1
            print(contador_numero, end=' ')
        print()
        
if __name__ == "__main__":
    run()