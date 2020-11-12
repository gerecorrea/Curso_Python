from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


class Conta:
    """Classe conta do banco."""
    codigo: int = 1001

    def __init__ (self: object, cliente: Cliente) -> None:
        """Construtor da classe conta."""
        self._numero: int = Conta.codigo
        self._cliente: Cliente = cliente
        self._saldo: float = 0.0
        self._limite: float = 100.0
        self._saldo_total: self._saldo + self._limite
        Conta.codigo += 1

    def __str__(self: object) -> str:
        """para deixar o print(conta) bem claro e do nosso jeito."""
        return f"Número da conta: {self.numero} \nCliente: {self.cliente.nome}" \
            f"\nSaldo total: {formata_float_str_moeda(self.saldo_total)}"


    @property
    def numero(self: object) -> int:
        return self._numero

    @property
    def cliente(self: object) -> Cliente:
        return self._cliente

    @property
    def saldo(self: object) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self._saldo = valor

    @property
    def limite(self: object) -> float:
        return self._limite

    @limite.setter
    def limite(self: object, limite: float) -> None:
        self._limite = limite

    @property
    def saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo = self.saldo + valor  # aciona o setter do saldo.
            # Aqui ele chamou saldo_total tbm, mas fiz diferente, o meu n precisa
            print("Depósito efetuado com sucesso.")
        else:
            print("Erro. Seu valor é inválido.")

    def sacar(self: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            # 0 < valor < self.saldo_total seria uma opção de escrever o if.
            if self.saldo >= valor:  # se seu saldo real é maior
                self.saldo = self.saldo - valor
            else:
                restante: float = self.saldo - valor  # para complementar a partir do limite
                self.limite = self.limite + restante  # pois restante deve ser negativo
                self.saldo = 0
            print("Saque efetuado com sucesso.")
        else:
            print(
                "Erro. Saque não realizado, seu saldo+limite não é suficiente "
                "ou seu saque foi de valor negativo."
            )

    def transferir(self: object, destino: object, valor: float) -> None:
        """Poderia usar o __future__ para definir destino como Conta."""
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                destino.saldo = destino.saldo + valor
            else:
                restante: float = self.saldo - valor
                self.limite = self.limite + restante # será neg ou zero.
                self.saldo = 0
                destino.saldo = destino.saldo + valor
        else:
            print("Erro. Valores insuficientes. Transferência não realizada")