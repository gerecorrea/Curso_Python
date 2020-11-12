"""
Debugger com fstrings.

Com o novo recurso podemos debuggar valores apenas cm o sinal de =

"""

def multiplica(num1: float, num2: float) -> float:
    return num1 * num2

resultado: float = multiplica(4.2345, 77.5454)
print(resultado)

# Forma de debuggar:

geek: str = 'Gere'
print(f"geek='{geek}'")  # isso aqui pode ser substituiído por:
print(f"{geek=}")  # por isso
print(f"{geek.upper()[::-1] = }")  # retorna em tela tbm o que foi realizado

