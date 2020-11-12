"""
Argumentos somente posicionais.

Uso de '/' e '*' nos argumentos para indicar que o que está a esq dele é
somente posicional, a direita não. Isso para o /
    Ou seja, não pode botar o nome do parametro=, somente o argumento padrão
    Mas a direito é oopcional
Para o *, indca que tudo a direita dele é obrigatorio declarar o nome do parametro
"""


def cumprimenta(nome: str, /, sobrenome: str, *, mensagem: str) -> str:
    """Tudo que tiver antes da barra é somente posicional."""
    return f"Olá, {nome} {sobrenome}, {mensagem}"


print(cumprimenta('Geremias', sobrenome='Correa', mensagem='Hello'))
