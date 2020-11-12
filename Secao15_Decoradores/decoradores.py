"""
Decorators (decoradores).

Decorators ->
    São funções
    Envolvem outras funções e aprimoram seus comportamentos
    Tbm são exemplos de Higher Order Function
    Tem uma sintaxe própria, usando @ (Syntatic Sugar/Açúcar sintático)

Function Decorator:
    Seria a funçaõ que é uma função decoradora
    O Simples uso do "@" seria apenas o decorador em si
    Quando se usa o @ implica que a função marcada será chamada primeiro

É útil para esclarecer sobre reutilizações de funções dentro de outras funções
    Como a necessidade de login (certa função) para acesso a certo serviço
    de uma aplicação (que é definido por uma função tbm) 
"""

# Decorators como funções (com sintaxe não recomendada):

def be_plite(funcao):
    """Função que retorna uma string de algo externo, além da chamada de outra
    função."""
    def being():
        print('Foi um prazer te conhecer')
        funcao()
    return being


def have_a_nice_day():
    """Função que retorna uma string."""
    print("Have a nice day")


teste = be_plite(have_a_nice_day)
teste()


# Decoratores com Syntatic Sugar:

def be_plite_sugar(funcao):
    """Agora utilizando o syntatic sugar"""
    def being_sugar():
        print('Foi um prazer te conhecer')
        funcao()
    return being_sugar


@be_plite_sugar
def have_a_nice_day_sugar():
    """Função que retorna uma string."""
    print("Have a nice day")


