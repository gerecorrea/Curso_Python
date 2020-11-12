"""Decatorators com diferentes assinaturas.

# Para situações de dois parametros quando se espera um, temos o uso de:
    Decorator pattern
    É a ideia de utilizar os *args e **kwargs nos parametros
    Permitindo essa flexibilidade
    Lembrando que args lançam uma tupla e kwargs um dicionário

"""

# Relembrando:
def scream(funcao):
    def upper(nome):
        return funcao(nome).upper()
    return upper


@scream
def hey(nome: str):
    """Com o @ ali, executa o scream primeiro."""
    return f'Olá, eu sou o {nome}'


@scream
def ordenar(principal: str, acompanhamento: str):
    return f'Gostaria de {principal} e {acompanhamento}'


print(hey('Angelina'))
# print(ordenar('picanha','batata frita'))  # N funciona por conta de 2 args


# Refatorando com o Decorator Pattern:
def scream_pattern(funcao):
    """Agora podemos variar os parâmetros."""
    def upper_pattern(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return upper_pattern


@scream_pattern
def ordenar_pattern(principal: str, acompanhamento: str):
    """Pedido, agora podendo chamar o novo scream."""
    return f'Gostaria de {principal} e {acompanhamento}'


print(ordenar_pattern('picanha', 'batata frita'))
print(ordenar_pattern(acompanhamento='picanha', principal='batata frita'))


# Decorator function com argumentos:
def verify_first_argument(value: str):
    def intern(funcao):
        def other(*args, **kwargs):
            if args and args[0] != value:
                return f"Incorreto! Primeiro argumento precisa ser {value}"
            return funcao(*args, **kwargs)
        return other
    return intern


@verify_first_argument('pizza')  # Implica que pizza precisa ser o 1º argumento
def favorite_food(*args):
    print(args)


print(favorite_food('lalala'))  # Não aceita
print(favorite_food('pizza', 'caldo de cana', 'lasanha'))  # Aceita