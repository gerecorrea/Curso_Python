"""

Escopo de variáveis

Escopo global x local
    É em relação ao contexto também, uma variável numa função pode ser global a função mas local ao contexto geral do código
    Assim como um variável dentro de uma condicional seria uma local

Lembrar da inferência de tipos/tipagem dinâmica
    O que permite a reatribuição de um tipo de variável para outro sem
    quaisquer problemas
"""

# Definindo uma variável no escopo global
variavel = 40

# Escopo local de uma variável qualquer dentro da condicional
if variavel > 20:
    var_local = 4.0

