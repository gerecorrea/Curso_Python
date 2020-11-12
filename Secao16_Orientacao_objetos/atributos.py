"""
Atributos. Aula longa de 1h20.

Três grupos de atributos:
    Atributos de instância - atributos declarados pelos parametros de instancia
    , ou seja, pelo método construtor
    Atributos de classe - atributos declarados diretamente na classe, então
    fora do construtor
    Atributos dinâmicos - atributo exclusivo da instância que o criou.

A palavra self é uma convenção de utilização, não necessariamente é o nome obg.

Em Python, por conveção, ficou estabelecido que todo atributo de uma classe é
público, podendo então ser acessado em todo o projeto. (não necessitando de 
getters, por exemplo)
Caso se queira demonstrar que determinado atributo deve ser tratado como
privado, deve ser utilizado "__" no início de seu nome
    Também conhecido como Name Mangling
Mas é apenas uma conveção, o Python não irá impedir o acesso aos atributos
sinalizados

"""


# BÁSICO - COM ATRIBUTOS DE INSTÂNCIA:
class ContaCorrente:
    """Classe Conta corrente." Apenas um espaço entre os defs aqui."""

    def __init__(self, numero: int, limite: int, saldo: float, cod: int):
        """Construtor."""
        # self para se referir ao próprio objeto
        self.numero = numero  # atributo público padrão 
        self.limite = limite
        self.saldo = saldo 
        self.__codigo_verificacao = cod  # Atributo privado pelo uso do __

    def mostra_cod(self):
        """MOstra o código que supostamente é privado da maneira correta."""
        print(f"Código ultrassecreto: {self.__codigo_verificacao}")


c1 = ContaCorrente(444, 100, 5.000, 373)
c2 = ContaCorrente(367234, 10000, 27.346, 287)
print(c1.limite)
# print(c1.__codigo_verificacao)  # Gera AttributeError, mas é apenas um nível
# de segurança que o Python faz
# Mas poderíamos:
# print(c1._ContaCorrente__codigo_verificacao)  # Assim é possível, mas errado
# Mas o correto seria:
c1.mostra_cod()

print(c2.numero)
c2.mostra_cod()


# MÉDIO - USO TBM DE ATRIBUTOS DE CLASSE:

class Produto:
    """Classe produto."""

    # Atributos de classe (fora do construtor)
    imposto = 1.10
    vendido = False
    contador = 0

    def __init__(self, nome: str, descricao: str, valor: float) -> None:
        """Construtor. Atribuindo dados não passados tbm."""
        self.id = Produto.contador + 1  # atributo id que atualiza automat.
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.id


prod1 = Produto("Renault Duster", "carro", 43.900)
print(f"Imposto sobre o {prod1.nome}: {prod1.imposto}")  # n correto
# Forma correta de acesso de um atributo de classe (global):
print(f"Forma correta de printar o atributo de classe: {Produto.imposto}")

print(prod1.id)
prod2 = Produto("Renault Clio", "carro", 23.900)
print(prod2.id)
print(Produto.contador)  # Sem utilização, apenas para verificação


# AGORA COM USO TBM DE ATRIBUTOS DINÂMICOS:
# usado a função produto anterior
prod2.peso = '5 kg'
print(prod2.peso)  # Não existe na classe, é apenas do prod2, criado posteriorm.
# Apesar disso, não parece mto o correto ou ideal, tanto que o Pylance reclama


# DELETANDO ATRIBUTOS:

print(prod2.__dict__)  # Imprime todas as informações de cda produto em um dict
del prod2.peso  # Deleta da instancia prod2 o atributo peso
# print(prod2.peso)  # Agora retorna atributeError
del prod2.valor  # Funciona tbm sem problema para atributos estáticos


# EXEMPLO EXTRA, NADA DE MAIS, SOMENTE COM ATRBITUOS PRIVADO E USO DO @PROPERTY:
class Lampada:
    """Classe lâmpada."""

    def __init__(self, voltagem: int, cor: int):
        """Declaração básica dos atributos, método construtor.
        Repare que aqui todos são supostamente privados
        Por conta disso são criados métodos getters para seus acessos."""
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    @property
    def voltagem(self):
        """método de get do voltagem."""
        return self.__voltagem

    @property
    def cor(self):
        """método de get da cor"""
        return self.__cor

    @property
    def ligada(self):
        """método de get do ligada."""
        return self.__ligada
