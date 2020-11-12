"""Criando sua própria versão de loop.


Apesar dos laços do Python serem ótimos, mas aqui estamos buscando entender
a fundo a ideia do funcionamento dos iteradores.


"""

# Loop comum:
for num in [1, 2, 3, 4, 5]:
    pass

# Criando seu próprio loop com iter:
def meu_for(iteravel: iter):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break