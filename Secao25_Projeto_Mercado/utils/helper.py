

def formata_float_str_moeda(valor: float):
    """Formata o float em string com 2 casas. Nem vou usar, dando erro"""
    # return f'R$ {valor:,.2f}'
    return f"R$ {round(valor, 2)}"

# formata_float_str_moeda(24.2323232)
