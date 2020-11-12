from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self._codigo: int = Produto.contador
        self._nome: str = nome
        self._preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self._codigo

    @property
    def nome(self: object) -> str:
        return self._nome

    @property
    def preco(self: object) -> float:
        return self._preco

    def __str__(self: object) -> str:
        return f"Código: {self.codigo} \nNome: {self.nome} \nPreço: R$ {self.preco}"
