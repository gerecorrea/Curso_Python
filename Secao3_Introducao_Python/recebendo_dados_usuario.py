'''

Recebendo dados do usuário (leitura de inputs)

'''
# Entrada de dados
nome = input("Qual seu nome? ")
idade = input("Qual sua idade?")
# Dá para fazer o print primeiro e depois outra linha com apenas atribuição do input com 
# parenteses vazios, mas assim é mais prático

# Exemplo input com uma linha para cda
idade = input('Qual sua idade?')

# Processamento

# Saída de dados
print ("\nNome: " +nome +"\nIdade: " +str(idade))

# Forma possível a partir do 3.7 e boa para quando trabalhado com muito texto e variáveis em conjunto:
print(f'\nA {nome} tem {idade} anos')

# Exemplo de cast float:
idade = float(idade)  # realizando um cast exemplo, também temos str(), int(), por exemplo
print("\nIdade em float: " +str(idade))

# Obs: Caso não queira que pule uma linha no print:
# print(conteudo, end='')