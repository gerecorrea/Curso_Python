"""
Métodos de data e hora.

função now() e today() (mesma coisa): retiornam a data e hora de hj
    Mas no now() podemos especificar um timezone (gmt)

instal biblioteca textblob
pip install textblob
"""

import datetime
from datetime import date
from textblob import TextBlob
import timeit


def formata_data(data: date):
    """Formata a data da forma br desejada."""
    if data.month == 1:
        return f"{data.day} de Janeiro de {data.year}"
    elif data.month == 2:
        return f"{data.day} de Fevereiro de {data.year}"
    elif data.month == 3:
        return f"{data.day} de Março de {data.year}"
    elif data.month == 4:
        return f"{data.day} de Abril de {data.year}"
    elif data.month == 5:
        return f"{data.day} de Maio de {data.year}"
    elif data.month == 6:
        return f"{data.day} de Junho de {data.year}"
    elif data.month == 7:
        return f"{data.day} de Julho de {data.year}"
    elif data.month == 8:
        return f"{data.day} de Agosto de {data.year}"
    elif data.month == 9:
        return f"{data.day} de Setembro de {data.year}"
    elif data.month == 10:
        return f"{data.day} de Outubro de {data.year}"
    else:
        return f"{data.day} de mês qualquer de {data.year}"


def formata_data2(data: date) -> str:
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}."
    # Obs:: precisa de internet para seu uso.


if __name__ == "__main__":    
    agora = datetime.datetime.now()
    print(agora)
    hoje = datetime.datetime.today()
    print(hoje)
    
    manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
    print(manutencao)  # quando der meia noite do próximo dia 


    # Encontrar o dia da semana - weekday():
    # os dias da semana nele começam em 0, sendo este segunda-feira
    print(manutencao.weekday())  # printa o dia da semana, sendo 0 segunda

    aniversario = "20/01/1997"
    aniversario = aniversario.split("/")
    print(aniversario)
    aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
    print(aniversario)
    if aniversario.weekday() == 0:
        print("Você nasceu numa segunda-feira")
    else:
        print("Você nasceu outro dia.")

    # Formatando a data para o formato que gostariamos

    hoje = datetime.datetime.today()
    hoje_formatado = hoje.strftime("%d/%m/%Y")  # formato para nosso padrão
    hoje_formatado = hoje.strftime("%d/%b/%Y")  # com 3 primeiras letras do mês
    hoje_formatado = hoje.strftime("%d/%B/%Y")  # com mês por inteiro
    hoje_formatado = hoje.strftime("Dia %d de %B de %Y")  # com mês por inteiro
    print(hoje_formatado)
    print(formata_data(hoje))

    # Usando textblob:
    print(formata_data2(hoje))

    nascimento = "20/01/1997"
    nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
    print(nascimento)
    # Ele faz direto, sem precisarmos converter a mão pra lista.

    # MARCANDO TEMPO DE EXEC DO NOSS CÓDIGO:

    # Loop for
    tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    # O primeiro parametro é a linha de comando em si e o segundo a qtd de vezes
    print(tempo)

    # List Comprehension
    tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
    # O primeiro parametro é a linha de comando em si e o segundo a qtd de vezes
    print(tempo)

    # Outra forma de marca o tempo de exec:
    import functools


    def teste(n: int):
        soma = 0
        for num in range(n * 200):
            soma = soma + num ** num + 4
        return soma

    print("Tempo de exec:", timeit.timeit(functools.partial(teste, 2), number=2000))
