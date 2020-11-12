"""
POO - Herança (Inheritance).

Vamos entender o que é herança, método super, etc

Herança -> É a ideia de um objeto que possui características identicas a um
outro objeto, ou seja, herda características dele, porém possui características
exclusivas suas também
    A sua ideia parte também da lógica de se reaproveitar código, além de
    extender suas classes e criação de relação entre elas.

Ex: Cliente possui nome, sobrenome, cpf e renda
Um funcionário herda o nome, sobrenome e cpf, mas possui tbm matrícula

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    - Super classe
    - Classe mãe
    - Classe pai
    - Classe base
    - Classe genérica

Sobreescrita de métodos (Overriding): são referentes a métodos que existem tan-
to na superclasse quanto na classe, então a sobreescrita de métooo permite nós
sobreescrevermos um método existente na superclasse para se adaptar de forma
mais específica a seu contexto atual.

Quando preciso, podemos acessar um método qualquer da super classe através de:
super().nomeDoMetodoDaSuperClasse(params)

OBS: aviso diego sobre acessos de herança x classe normal:
O acesso aos aitrbutos da classe pai por pate das classes filhas para evitar os
erros do PyLance (por questão de boa escrita de código), devem ser declarados
como protected, ou seja, com apenas um underline (_)

Quanto possuo somente uma classe normal, sem filhos herdados delas, tudo bem
declarar as variáveis privadas (__), porém quando possuo classes filhas e essas
precisarão acessar tais atributos, o correto é criar como protected (_)

Na aula de MRO utilizando o protected pros atributos, dar uma olhada lá 

"""


class Pessoa:

    def __init__(self, nome: str, sobrenome: str, cpf: str) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self._cpf = cpf  # Este eu declaro como protected, repare no acesso dele
        # posteriormente, como que é diferente.
    
    def nome_completo(self) -> str:
        """Método para ser chamado nas outras classes. Na cliente chama este,
        enquanto na Funcionário foi feito um outro (override) para chamada."""
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa): 
    """Classe cliente. Ela herda de Pesoa, por isso o (Pessoa).
    Com o super() consigo acesso a qualquer elemento da superclasse."""

    def __init__(self, nome: str, sobrenome: str, cpf: str, renda: float) -> None:
        super().__init__(nome, sobrenome, cpf)  # Herda de pessoa
        # OU: Pessoa.__init__(self, nome, sobrenome, cpf)  # Herda de pessoa
        self.__renda = renda


    """Aqui não temos o método nome completo, mas caso chame para o cliente, ele
    ouvirá o da superclasse, que é o que já existe."""
    # ou:
    def nome_completo2(self) -> None:
        print(super().nome_completo())  # Chamando um método da superclasse
    
    @property
    def cpf(self):
        return self._cpf

class Funcionario(Pessoa): 
    """Classe funcionário. Ela herda de Pessoa."""

    def __init__(self, nome: str, sobrenome: str, cpf: str, matricula: int) -> None:
        super().__init__(nome, sobrenome, cpf)  # Herda de pessoa
        self.__matricula = matricula

    def nome_completo(self):
        """Método sobreescrito ao original, ouvindo a este e não aao da superclasse"""
        return f"Funcionário: {self.__matricula}. Nome: {self._Pessoa__nome} {self._Pessoa__sobrenome}"


if __name__ == "__main__":
    pessoa1 = Pessoa('Geremias', 'Correa', '123.456.789-67') 
    cliente1 = Cliente('Geremias', 'Correa', '123.343.434-75', 5000)
    funcionario1 = Funcionario('Stephen', 'Hawking', '981.323.323-53', 1234)
    print(cliente1.nome_completo())
    print(funcionario1.nome_completo())
    print(cliente1.nome_completo2())
    print(cliente1.cpf)
