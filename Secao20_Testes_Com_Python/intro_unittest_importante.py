"""
Introduçao ao método Unittest - o mais importante dessa seção.

Unittest -> Testes unitários, que são a forma de se testar códigos individuais

Esses unidades individuais podem ser: funções, métodos, classes, módulos.

Para criar nossos testes, criamos classes que herdam do unittest.TestCase e a
partir de então 

Usando aqui os arquivos atividades.py teste.py

Métodos exemplo existentes:
    Existem vários métodos (procurar "unittest métodos" na internet).
    assertEqual(a,b)    a == b
    assertNotEqual(a,b) a != b
    assert True(a)      a é true
    assertIs(a,b)       a é b
    assertIfNone(x)     x é None
    assertIn(a,b)       a está em b (casos de lista, tupla, etc)
    assertIsIstance(a,b)a é instancia de b
    Obs: todas elas tem negação, com Not antes da lógica de operação.

    Alguns são assertEqual(a,b), assertNotEqual(a,b), assertTrue(a,b)
    assertIs(s), etc.

    Para executar os testes, ir no arquivo testes.py, eles estão lá
    Sua execução é no terminal python3.8 testes.py

    No terminal, retorna '.' para testes que passaram e F para falhos.

    
"""

# Prática - utilizando a abordagem TDD:
    # Lança $ python3.8 testes.py -v
    # ou seja, lança a flag -v, que dá uma maior detalhamento
