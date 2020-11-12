"""

Todas as utilizações aqui são válidas e úteis
    O Diego disse que tudo é possível de ser utilziado e válido sim
    Tentar se adaptar a tais usos

Reparado durante sua realização:
# uma carta é uma tupla de string string
# e uma baralho é uma lista de cartas
# 
"""
from typing import List, Tuple, Dict, Set
import random


# nomes: list = ['Geek', 'University']  # Mas falta o tipo do elemento da lista
nomes2: List[str] = ['Geek', 'University'] 
versoes: Tuple[int, int] = (3, 4, 7)
opcoes: Dict[str, bool] = {'ar': True, 'bc': False}
valores: Set[int] = {3, 4, 5, 6}

# www.alt-codes.net/suit-cards.php
naipes = '♠ ♥ ♣ ♦'.split()
cartas = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
print(naipes)
print(cartas)

# Caso queira usar, para definir (alias) os tipos de annotation do type hinting
CARTA = Tuple[str, str]  # não to usando mas é útil
BARALHO = List[CARTA]  # não to usando mas é útil


def cria_baralho(aleatorio: bool = False) -> List[Tuple[str, str]]:
    """Cria um baralho com 52 cartas."""
    baralho: List[Tuple[str, str]] = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]], List[Tuple[str, str]], List[Tuple[str, str]]]:
    """Gerencia a mão de cartas de acordo com o baralho gerado. 4 jogadores.
    Retorno poderia ser Tuple[BARALHO, BARALHO, BARALHO, BARALHO]."""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


baralho = cria_baralho()
print(distribuir_cartas(baralho))


def jogar():
    """Inicia um jogo de cartas para 4 jogadores."""
    cartas: List[Tuple[str, str]] = cria_baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, List[Tuple[str, str]]] = {jog: mao for jog, mao in zip(jogadores, distribuir_cartas(cartas))}
    # aqui jog = jogadores e mao = maos

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f"{jogador}: {carta}:")
        # aqui j = jogador, c = carta


print("Jogando")
jogar()