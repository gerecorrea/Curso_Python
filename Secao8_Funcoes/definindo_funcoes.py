"""

Definindo funções.

Criar pequenas parte de código para execução de tarefas específicas
Útil para tarefas repetitivas
Útil para tarefas complexas e adaptativas ao nosso contexto
Pode se utilizar funções dentro de funções

Obs: Se você escrever uma função que realiza várias tarefas dentro dela é bom
fazer uma verificação para que a função seja simplificada

No Python são várias que utilizamos, como print(), append(), len(), max(), etc
    Porém podemos executar funções específicas para o nosso contexto

Dicas:
    Procure escrever funções simples
    DRY - don't repeat yourself
    Utilizar um __main__ chamando a função inicial do código, n deixar jogado

O nome de uma função é defini por "def"

Nomenclaturas - dicas:
    nome_da_funcao -> sempre com letras minusculas
        separado por underline (snake case)
    parametros_de_entrada -> Opcionais, separados por vírgulas (caso + de 1)
    bloco_de_funcao -> Trecho onde ocorre o processamento da função

"""

# Exemplos de utilização de funções:

cores = ['branco', 'amarelo', 'azul', 'preto', 'vermelho', 'verde']

# Utilizando funções integradas (built-in) do Python
print(cores)
cores.append('roxo')  # Função para dados do tipo lista, senão retorna erro
print(cores)

# Definindo uma função:


def diz_oi():
    """Docstring."""
    print('Oi')
    print('Tudo bem?')
    print('É hora de dar tchau!')

# Usar um main ou, se sem ele, chamar ela como acima

# Chamada de execução:
# diz_oi()


if __name__ == "__main__":
    diz_oi()
