"""

int, str, float, List, set, Dict, etc

Mas aqui temos:
- Literal type: forçado a um ou mais parâmetros literais específicos
- Union: retorna um ou outro, deixa claro que pode ter mais de 1 tipo
- Final: para criar constantes. Também pode ser usado como @final como decorator em métodos
    Avisando que nenhuma classe pode sobreescrever/extender elas!
- Typed dictionaries: cria a classe como elementos do tipo dict: chave e valor
- Protocol: 
"""

from typing import Literal, Union, Final, TypedDict, Protocol


def dobro(valor: int) -> int:
    return valor * 2


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    """precisa retorna ou a string conectado ou descontectado."""
    return 'conectado'


def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1 + num2}')
    else:
        raise ValueError(f"operação inválida {operacao!r}")
        # Retorna o tipo da operação entre aspas, parece.


def calcula_v2(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1 + num2}')
    elif operacao == '-':
        print(f'{num1 - num2}')
    else:
        raise ValueError(f"operação inválida {operacao!r}")
        # Retorna o tipo da operação entre aspas, parece.


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f"O valor {resultado} é muito grande!"
    return resultado

# Literal:
calcula_v1('+', 6, 4)
# calcula_v1('-', 6, 4)
calcula_v2('+', 5, 2)
# calcula_v2('*', 5, 2)

# Union:
print(soma(34, 2))
print(soma(54, 2))

# Final:
NOME: Final = 'Geek'  # forma correta, sem dizer que é tipo Final gera erro.
NOME2: str = 'Geek2' # Deixando claro o tipo tbm, mas aí não é constante!!!
print(NOME)
print(NOME2)

# TypedDict:


class CursoPython(TypedDict):
    """Os valores são criados como tipo dict."""
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)

# Protocols: 


class Curso(Protocol):
    """Protocolos não podem ser inicializados (sem init)."""
    titulo: str
    

def estudar(valor: Curso) -> None:
    print(f"Estou fazendo o curso {valor.titulo}")

v1 = Curso()
v1.titulo = 'Python'
estudar(v1)

