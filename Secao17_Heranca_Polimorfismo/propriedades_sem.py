"""
POO - Propriedades (Properties).

Getters e setters em conjunto da classe usada na aual de abstração e encaps..

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

    def get_saldo(self):
        """Função que apenas retorna os valores dos atributos (getter)."""
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_numero(self):
        return self.__numero

    def set_limite(self, limite: float):
        """Altera o limite atual da conta por um setter.
        Para os outros não criei pq não tem sentido, e é só pra ex."""
        self.__limite = limite

    def get_limite(self):
        return self.__limite

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
    soma = c1.get_saldo() + c2.get_saldo()
    print(f"O saldo soma das duas é: {soma}. ")
    print(f"Limite atual: " {c1.get_limite()})
    c1.set_limite(1200)
    print(f"Limite atual: " {c1.get_limite()})