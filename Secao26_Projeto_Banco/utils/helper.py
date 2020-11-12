from datetime import date
from datetime import datetime


def date_para_str(data: date) -> str:
    """Data de formato iso para string especificada."""
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    """Data de formato nosso (br) para iso padrão."""
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    """Moeda para formato. Antes deu ruim, qlqr coisa fazer a mão."""
    return f'R$ {valor:,.2f}'


# Testes:
# print(str_para_date('30/08/2020'))
# print(date_para_str(str_para_date('30/08/2020')))