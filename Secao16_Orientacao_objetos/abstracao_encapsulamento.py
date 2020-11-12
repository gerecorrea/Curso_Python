"""
POO - Abstração e encapsulamento.

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico
e hierárquico utilizando classes.

Encapsular -> abstrair de forma direta e protegida o dado objetificado.

Em Python temos o fenomeno Name Mangling, que faz uma alteração na forma de se
acessar os elementos privados, porém não impede.
    instancia._NomeClasse__atributo

Abstração, em POO, é o ator de expor apenas dados relevantes de um classes
    Escondendo atributos e métodos privados de usuário

Aqui vamos fazer tbm a relação entre duas classes através de uam função de
transferência

Também utilizei o import da lib __future__ para parametro de uma classe dentro
de um método da própria classe
    Caso fosse uma função externa, não seria necessário tal uso, seria apenas
    : NomeClasse

"""
from __future__ import annotations


class Account:

    contador = 400

    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        """Constructor from the class Account. All the atributtes are public, so
        they all are easily changeble.
        Now, all the atributtes are private."""
        # self.titular = titular
        # self.saldo = saldo
        # self.limite = limite
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__numero = Account.contador + 1
        Account.contador = self.__numero

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


c1 = Account('Gere', 1500.00, 500.00)
c2 = Account('Gaby', 700.00, 500.00)
# print(c1.numero)  # Now they are private, so can't acess this way
c1.deposit(1500.34)
c1.extract()
c1.take(400.52)
c1.extract()
c1.take(700.52)
c1.extract()
print("Todos os dados:\n", c1.__dict__)
print("Todos os dados:\n", c2.__dict__)

# Criando uma relação entre as classes com transferência e usando a função:
c1.transference(400, c2)  # valor, conta objeto de destino
print("Todos os dados:\n", c1.__dict__)
print("Todos os dados:\n", c2.__dict__)