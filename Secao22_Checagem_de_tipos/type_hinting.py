"""
Type hinting.

É a ideia de dar a ideia do tipo de dado recebido no parametro e do tipo de 
retorno.
    Entra no Python 3.5
    Já faço uso desde o início do curso.
    É importante entender a tipagem dinâmica
    Ajuda e muito aos desenvolvedores e a IDE para ter um controle e visão melhor 
    do que está acontecendo.
    Não costumava usar para declaração/atribuição de varia´veis, assim como pas-
    -sar nos argumentos de chamadas, aparentemente é o ideal, sempre q possível

Recomenda-se sempre o uso do type hinting
    Inclusive é conhecido como um recurso avançado do Python, fazer uso dele
    é de notável aprendizado e reconhecimento quanto a saber sobre Python avanc.

Prós e contras (de outra aula) do Type hinting:
    Obs: como utilizo diversas extensões, qualquer erro simples dele a IDE me 
    retorna. Um tanto quanto diferente do mostrado no vídeo
    Vantagens:
        Permite maior controle de código
        Fica mais claro para outros desenvolvedores e mesmo apra você
        Deixa o software mais robusto

    Desvantagem:
        Somente na 3.7 que o recurso se torna completo
        Deixa o código ainda um pouco mais lento (um pouco só)
        Se fizer o uso do mypy para checagem, ele só checa os que fazem uso do
        type hinting.

Annotations:
    É a ideia de fazer anotações, como dizer que retorno da função é x, usar
    o docstring, utilização correta dos espaços, etc. 
        Tudo que aumenta a clareza do código.

    Correto:
        texto: str
        ) -> str:
        alinhamento: tipo = valor
        nome: str = "Geek Un"
        ativo: bool = True
        fone: int

    Incorreto:
        text:str
        texto : str
        )->str:
        )-> str:
        ) ->str:
        alinhamento:tipo=valor
        alinhamento: tipo=valor
        alinhetamento:tipo = valor (etcc)

"""
import math


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


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


if __name__ == "__main__":
    print(cump('JJ'))
    print(cabecalho('geek un', True))
    print(cabecalho('geek un', False))
    print(circunferencia(5))
    print(circunferencia.__annotations__)  # Retorna as anotações de código esperadas

