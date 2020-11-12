"""
Métodos.

Métodos (funções) -> Representam os comportamentos de cada objeto
    As ações que o objeto pode realizar no sistema (as funções padrão)

Dois grupos:
    Métodos de instância - pois precisa ter uma instancia do objeto para ter
    acesso a ele
    Métodos de classe - são possíveis de serem acessados sem precisar, necessa
    riamente, da instanciação do objeto em si.
        Utilizam o "cls" ao invés do "self"

O método dunder init (__init__) é um método especial chamado de construtor
    Constrói a classe/objeto

Por mais que possam criar nossas próprias funções utilizando dunder, não é
aconselhado

Métodos privados são realizados com uso do "__" no início do nome, só devem ser
acessados de dentro da classe.

Métodos estáicos: Repare que não tem o self e precisa do @staticmethod
    Está mais no final do código

install biblioteca para criptografia (senhas e tal):
pip install passlib

"""
from passlib.hash import pbkdf2_sha256 as cryp


def encripta(senha: str) -> str:
    """Função para evitar o aviso de erro de tipo desconhecido na classe."""
    return cryp.hash(senha, rounds=200000, salt_size=16)  # noqa
    # Tem tbm encrypt
    # Para se corrigir esse problema de retorno, pesquisar por pela criação
    # de uma arquivo para definição de tipos. Tem o uso do # noqa para ignorar
    # a linha, masss precisa ter instalado pylama como extensão no vscode.print(interr1.estado_lampada)

# CLASSE BÁSICA COM MÉTODOS DE INSTÂNCIA:

class ContaCorrente:
    """Classe Conta Corrente."""

    contador = 4999
    id = 0

    def __init__(self, limite: float, saldo: float, senha: str) -> None:
        """Construtur, todos como privados."""
        self.__numero = ContaCorrente.contador + 1
        self.__id = ContaCorrente.id + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__senha = encripta(senha)
        """os 2 parametros extras o primeiro é para embaralhamento (qt +, mlr)
        e a segunda o tamanho dela."""
        ContaCorrente.contador = self.__numero
        ContaCorrente.id = self.__id

    @property
    def get_limite(self) -> float:
        """Exemplo de um getter de um atributo privado. Não obrigatório"""
        return self.__limite

    @property  # Definir como propriedade define que pode ser chamado sem ()
    def get_senha(self) -> str:
        """Getter exemplo da senha criptografada."""
        return self.__senha

    def checa_senha(self, senha: str) -> bool:
        """Recebe a senha criptografada e verifica se são iguais."""
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def min_saldo(self) -> None:
        """Define o saldo mínimo possível ao final do mês. Método de inst."""
        print(
            f"Saldo mínimo possível ao final do mês: "
            f"R$ {self.__saldo - self.__limite}"
        )

    def deposito(self, valor: float) -> None:
        "Função que realiza um depósito. Método de instância."
        self.__saldo = self.__saldo + valor
        print(
            f"Depósito de R$ {valor} realizado.\n"
            f"Seu saldo agora é de R$ {self.__saldo}."
        )

    @classmethod
    def verifica_conta_atual(cls) -> None:
        """Para usar o método de classe. Repare que precisa do @classmethod"""
        print(f"O número atual de conta no sistema é {cls.contador}")

    def __modifica_padrao_conta(self) -> None:
        """Função que modifica o atributo geral da classe. Seria um método
        privado criado, por isso o uso do __ no início.
        Então só deve ser possível acessar ele de dentro da classe.
        Caso tente fora, é possível, com uso do nome._Classe__metodo(), mas é 
        indesejado fazer isso."""
        self.__contador = self.__contador + 2000

    @staticmethod
    def call() -> str:
        """Função definição, para exemplificar o método estático.
        Repare que não tem o self e precisa do @staticmethod"""
        return choice('Hey', 'sad', 'hello')


c1 = ContaCorrente(1300, 10000, '12345')
c1.min_saldo()
c1.deposito(4500)
print("Senhas iguais: ", c1.checa_senha("12345"))  # vai retornar True
print("Senhas iguais: ", c1.checa_senha("123456"))  # vai retornar False
print(f"Senha: {c1.get_senha}")
# print(c1.get_limite())


ContaCorrente.verifica_conta_atual()  # Forma correta para class method
c1.verifica_conta_atual()  # Possível, mas incorreto, pois é atributo geral
