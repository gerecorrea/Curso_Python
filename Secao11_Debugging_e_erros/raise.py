"""
Levantando os próprios erros com o raise.

Utilizado para prever alguma violação de regra posível no código

raise -> Lança exceções

OBS: ele não é uma função, é uma palavra reservada (assim como def, ou outra)

O uso do raise é aplicável para poder criar suas próprias exceções e mensagens
de erro que se aplicam ao nosso contexto e aplicação

Sintaxe geral:

raise TipoDoErro('Mensagem de erro')

OBS: O raise finaliza a função. Nada após o raise é executado.

"""

# Ex: raise ValueError('Valor incorreto.')


def colore(texto: str, cor: str) -> None:
    cores = ('verde', 'preto', 'roxo','azul')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string.')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string.')
    if cor not in cores:
        raise ValueError(f"A cor precisa ser uma entre: {cores}")
    print(f"O Texto {texto} será impresso na cor {cor}.")


if __name__ == "__main__":
    # colore('Geek', 'azul')
    # colore(2, 'preto')
    # colore(2, 4)
    colore('GG', 'branco')
