from datetime import date
from utils.helper import date_para_str, str_para_date


class Cliente:
    """Classe cliente do banco."""
    contador: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nasc: str) -> None:
        """Construtor da classe cliente."""
        self._codigo: int = Cliente.contador
        self._nome: str = nome
        self._email: str = email
        self._cpf: str = cpf
        self._data_nasc: date = str_para_date(data_nasc)
        self._data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:
        self._codigo

    @property
    def nome(self: object) -> str:
        return self._nome

    @property
    def email(self: object) -> str:
        return self._email

    @property
    def cpf(self: object) -> str:
        return self._cpf

    @property
    def data_nasc(self: object) -> str:
        return date_para_str(self._data_nasc)

    @property
    def data_cadastro(self: object) -> str:
        return date_para_str(self._data_cadastro)

    def __str__(self: object) -> str:
        return f"Código: {self.codigo} \nNome: {self.nome} \nData de Nasc.: " \
        f"{self.data_nasc} \nCadastro: {self._data_cadastro}"