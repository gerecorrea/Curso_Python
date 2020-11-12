"""
O que é a orientação a objetos

Apenas revisando caso tenha algo específico útil do python para botar aqui.

Objetivo de mapear objetos do mundo real para modelos computacionais
    Representado suas características e comportamentos de forma clara e
    de representatividade/modelagem válida
    É um paradigma de programação

Elementos:
    Classe -> É o modelo do mundo real, como um todo, representado
    Atributos -> São características do objeto. Podem ter nenhum a vários
    Métodos -> São as funções existentes dentro de uma classe
    Construtor -> É o método básico inicial de toda classe
        Ele determina/atribui as características básicas de criação da classe
    Instâncias -> São os objetos/instâncias criados de determinada classe

"""


# Ex simples:

class Produto:
    """Class produto ex."""

    pass


ps4 = Produto()
print(ps4)  # Printa o tipo do ps4 - saída: é um objeto
