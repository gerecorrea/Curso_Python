"""
Trabalhando com deltas de data e hora.

É a diferença entre uam data e outra
"""

import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2021, 3, 3, 0)

# Calculando o delta:
tempo_para_evento = aniversario - data_hoje
print(tempo_para_evento)
print(f"Faltam {tempo_para_evento.days} dias para o evento.")
print(f"Faltam {(tempo_para_evento.days * 24) + tempo_para_evento.seconds // 60 // 60} horas para o evento.")

# Criando um delta para vencimento, por ex:
data_da_compra = datetime.datetime.now()
regra_boleto = datetime.timedelta(days=3)  # a partir da data atual, adc 3 dias
vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)
