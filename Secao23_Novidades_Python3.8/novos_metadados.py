"""



"""


from importlib import metadata

# Podemos verificar a versão de qlqr pacote com eles
print(metadata.version('pip'))

# Também ver as versões disponíveis em qualquer pacote
print(list(metadados_pip := metadata.metadata('pip')))

# Qtd de arquivo em uma lib:
print(f"Quantidade de pacotes pip: {len(metadata.files('pip'))}")

# Verificar o que certo pacote requer (precisa estar instalado para verif.):
print(metadata.requires('django'))