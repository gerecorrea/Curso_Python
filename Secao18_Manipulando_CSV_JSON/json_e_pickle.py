"""
Trabalhando com JSON e Pickle.

JSON -> Javascript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
    (Twitter, Facebook, Youtube, ...) e terceiro (desenvolvedores)

Para trabalhar com pickle com json precisa instalar a biblioteca:
pip install jsonpickle  # ok

"""

import json
import jsonpickle

ret = json.dumps(['produto', {'PS4': ('2TB', 'Novo', '220V', 2340)}])
# o dumps deixa a saída redonda parao  formato json
print(ret)


class Gato:

    def __init__(self, nome: str, raca: str):
        self._nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self._nome

    @property
    def raca(self):
        return self._raca

felix = Gato('Felix', 'Vira-lata')
print(felix.__dict__)
ret = json.dumps(felix.__dict__)
print(ret)

# Escrevendo no arquivo json/pickle:
with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)  # jsonpickle encode
    arquivo.write(ret)
    print(ret)

# Lendo o arquivo json/pickle:
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)  # jsonpickle decode
    print(ret)
    print(ret.nome)
    print(ret.raca)

