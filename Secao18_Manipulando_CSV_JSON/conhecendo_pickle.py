"""
Conhecendo o Pickle.

A função do Pickle é realizar o seguinte processo:

Objeto Python - > Binarização

Binarização -> Objeto Python

Este processo é chamada de serialização/deserialização

#OBS: O módulo Pickel não é seguro contra dados maliciosos e desta forma
não é recomendado trabalhar com arquivos pickle vindos de outras pessoas
que você não ou conheça ou então de fontes desconhecidas

Se tentar abrir o arquivo, como é em binário (estão serializados).
    Em casos de segurança, quando necessário, é recomendado realizar a escrita
    em arquivos pickle, para não terem acesso visível de forma fácil.
"""
import pickle


class Animal(object):
    def __init__(self, nome: str) -> None:
        self._nome = nome  # protected

    def falar(self) -> None:
        raise NotImplementedError('A classe filha implementa tal método.')

    def comer(self) -> None:
        print(f"{self._nome} está comendo.")


class Cachorro(Animal):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)

    def falar(self) -> None:
        print(f"{self._nome} fala au au.")


class Rato(Animal):

    def __init__(self, nome: str) -> None:
        super().__init__(nome)


if __name__ == "__main__":
    felix = Cachorro('Felix')
    quinn = Rato('Quinn')

    # escrita para arquivo pickle:
    with open('animais.pickle', 'wb') as arquivo:
        # wb é write binary
        pickle.dump((felix, quinn), arquivo)  # dump recebe o obj e o arquivo

    # leitura de dados em arquivos pickle:
    with open('animais.pickle', 'rb') as arquivo:
        rato, cachorro = pickle.load(arquivo)
        print(f"O gato chama-se {rato._nome}")
        print(cachorro.comer())