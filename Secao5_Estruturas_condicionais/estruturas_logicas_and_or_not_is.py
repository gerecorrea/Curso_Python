"""

Estruturas lógicas: and(e), or(ou), not (não) e is(é).

Operadores unários: not e is
Operadores binários: and e or

"""
ativo = True
logado = False

if ativo and logado:
    print("Bem-vindo, usuário")
else:
    print("Você precisa se logar para acessar seus dados")

if ativo and not logado:
    # Equivalente a ativo == True and logado == False
    print("Acesso a página, mas não aos dados de usuário")
else:
    print("Error404")

if ativo is True:
    print("Está ativo")
elif ativo is not True:
    print("Não está ativo")
