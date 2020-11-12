def comer(comida: str, saudavel: bool) -> str:
    if saudavel:
        return 'Estou comendo por conta da dieta.'
    return 'fome de commida gostosa.'


def dormir(num_horas: int) -> str:
    if num_horas > 8:
        return 'Droga, dormi demais.'
    else:
        return 'Continuo cansado, dormi pouco.'


def nome(nome: str) -> bool:
    if nome == 'Geremias Correa':
        return True
    return False