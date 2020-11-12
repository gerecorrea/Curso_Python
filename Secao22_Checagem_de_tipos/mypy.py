"""
MyPy.

Nasceu com a abordagem de er uma nova linguagem de programação
    Mas acabou por se tornar o checador de tipos oficial da linguagem

Foi instalado: pip install mypy

Utilizando o Type hinting permite a checagem de tipos com o MyPy
    Permite programar melhor softwares.

OBS: usando código da aula passada
"""


# Exemplo ridículo demonstrativo.
def cump(nome: str) -> str:
    return f"Olá, {nome}"


# Desafio
def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')
        # vai centralizar o conteudo, dado que serão criados # a totalizar 50
        # caracteres, ficando o conteudo no meio.


if __name__ == "__main__":
    print(cump('JJ'))
    print(cabecalho('geek un', True))
    print(cabecalho('geek un', False))

