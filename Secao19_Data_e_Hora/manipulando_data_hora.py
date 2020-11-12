"""
Manipulando data e hora.

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado de 'datetime'

variáveis possíveis da classe: 
    year, month, day, hour, minute, second, microssecond

"""

import datetime


if __name__ == "__main__":
    print(dir(datetime))
    print(datetime.MAXYEAR)  # Max 9999
    print(datetime.MINYEAR)  # Min 1
    # Temos tbm disponível a classe datetime, qndo importado o módulo
        # A classe tem mesmo nome, por isso é datetime.datetime
    print(datetime.datetime.now())  # ano, mes, dia ' ' hora:min:seg
    print(repr(datetime.datetime.now()))  
    # variáveis possíveis: year, month, day, hour, minute, second, microssecond
    
    # Fazer um replace para ajustar os tempos:

    inicio = datetime.datetime.now()
    print(f"Início: {inicio}")
    inicio = inicio.replace(hour=16, minute=0, microsecond=0, day=13)
    print(inicio)
    print(datetime.datetime.now().replace(hour=15, year=2000))  # sendo mais direto

    # Criando uma data hora:

    evento = datetime.datetime(2019, 1, 1, 0)
    print(evento)
    nascimento = '20/01/1997'
    date = nascimento.split('/')  # cria um array de string separando pela / na string
    print(date)  # [0] = dia, [1] = mes, [2] = ano
    novo_evento = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
    print(novo_evento)  # output é a data especificada com a hora zerada

    # Acessando individualmente os elementos de data e hora:
    print(novo_evento.year)
    print(novo_evento.month)
    print(novo_evento.hour)
