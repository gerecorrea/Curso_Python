"""
Try Except.

Similar ao Try Catch de outras linguagens, como Java e C++

Utilizado o bloco try/except para tratar erros que podem ocorrer no nosso cod.
Previindo assim que o programa pare de funcionar e recebe este mensagens de
erros inesperados

Dado que muitos erros geram falta de confiança do usuário na aplicação
    Assim como maior vulnerabilidade a acesso de crackers
    Utilizar o try except melhora tais contextos de problemas

Sintaxe:

try:
    // execute
except:
    // o que deve ser feito e caso de problema

# Exemplo 1 - tratando um erro de forma genérica:

try:
    geek()  # NameError
except:
    print("Vish, deu problema!")

OBS: Tratar o erro de forma genérica, não é o ideal
    É válido ser claro e específico na motivação da geração do erro
    Assim como deixar claro qual exceçõa é (como, por ex, NameError, como aba)

Exemplo 2 - tratando um erro com o tipo definido dele e mensagem mais especif:

try:
    geek()
except NameError:
    print("Você está utilizando uma função inexistente.")

OBS: Podemos fazer um 'as err' para pegar o erro gerado e retornar ao user

Exemplo 3 - tratando um erro especifico e com detalhes do erro:

try:
    len(5)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")

Exemplo 4 - tratando erros com mais de um except:

try:
    len(5)
except NameError as erra:
    print(f"Deu NameError: {erra}")  # Algo como usar algo que não está decl.
except TypeError as errb:
    print(f"Deu um TypeError: {errb}.")
except:
    print(f"Outro erro inesperado!")


"""

# Para retorno de dicionário na função, assim como tipo None como Optional
from typing import Dict, Optional, Union

def pega_valor(dicionario: str, chave: str) -> Optional[Union[str, Dict[str, str]]]:
    """Função que pega o valor. O retorno é um dict de chave str e valor str"""
    # Além disso, como pode retornar o tipo None, então deve ter um Option
    # Optional porque é opcional então retornar o dicionário
    # além disso, pode retornar tipo string, então dentro do optional é precis
    # deixar claro que pode retornar ou str ou um dicionário    
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return print('TypeError')


if __name__ == "__main__":
    dic = {'nome': 'Geek'}
    print(pega_valor(dic, "nome"))
    print(pega_valor(dic, 8))