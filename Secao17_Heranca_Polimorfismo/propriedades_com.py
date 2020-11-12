"""
POO - Propriedades (Properties).

Getters e setters em conjunto da classe usada na aual de abstração e encaps..

Essa refatorando a classe anterior utilizando propriedades (decorators)!! 
@property para atributos, como se fosse um método
Mas o acesso ao atributo é sem os paranteses!!
Também do @atributo.setter, funcionando como método setter

OBS: aviso para depois colocando aqui tbm:
O acesso aos aitrbutos da classe pai por pate das classes filhas para evitar os
erros do PyLance (por questão de boa escrita de código), devem ser declarados
como protected, ou seja, com apenas um underline (_)

Quanto possuo somente uma classe normal, sem filhos herdados delas, tudo bem
declarar as variáveis privadas (__), porém quando possuo classes filhas e essas
precisarão acessar tais atributos, o correto é criar como protected (_)

Na aula de MRO utilizo o protected nos atributos, dar uma olhada lá

"""
from __future__ import annotations


class Account:

    contador = 400

    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        """Constructor from the class Account.
        Now, all the atributtes are private."""
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__numero = Account.contador + 1
        Account.contador = self.__numero

    @property
    def numero(self):
        return self.__numero

    @property 
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo

    @property 
    def titular(self):
        return self.__titular

    @limite.setter 
    def limite(self, limite: float):
        """Docstring setter de limite."""
        self.__limite = limite

    @property
    def valor_total(self):
        """Cria-se um atributo de algo que não é atributo, sem problemas."""
        return self.__saldo + self.__limite

    def extract(self) -> None:
        """To see the actual extract."""
        print(f"Saldo atual de: {self.__saldo}\nTitular: {self.__titular}")

    def deposit(self, valor: float) -> None:
        """Make a deposit in the account."""
        self.__saldo += valor

    def take(self, valor: float) -> None:
        """Take a value from the account."""
        if(valor > self.__limite):
            print(f"Saque maior que o limite de {self.__limite} permitido.")
        elif self.__saldo - valor < 0:
            print(f"Você não tem saldo suficiente para o saque deste valor")
        else:
            self.__saldo -= valor
            print(
                f"Saque de {valor} efetuado com sucesso! Seu saldo agora "
                f"é de {self.__saldo}"
            )

    def transference(self, valor: float, conta_destino: Account) -> None:
        """Transference between two accounts.
        Was imported __future__ lib to recognize future calls of the class
        parameter Account in this function inside Account class."""
        self.__saldo -= valor + 10  # 10 is the transference tax, for example
        conta_destino.__saldo += valor


if __name__ == "__main__":
    c1 = Account('Gere', 1500.00, 500.00)
    c2 = Account('Gaby', 700.00, 500.00)
    print(c1.extract())
    print(c2.extract())
    soma = c1.saldo + c2.saldo
    print(f"O saldo soma das duas é: {soma}. ")
    print(f"Limite atual: {c1.limite}")  # acessndo via propriedades
    c1.limite = 1300  # Atribuindo novo limite usando propriedades
    print(f"Limite atual: {c1.limite}")
