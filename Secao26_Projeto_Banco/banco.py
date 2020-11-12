from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta


contas: List[Conta] = []


def menu() -> None:
    """Função menu básica de operação."""
    print ("######################################")
    print ("################# ATM ################")
    print ("######################################")

    print("Selecione uma opção no menu: ")
    print("[1] - Criar conta")
    print("[2] - Efetuar saque")
    print("[3] - Efetuar depósito")
    print("[4] - Efetuar transferência")
    print("[5] - Listar contas")
    print("[6] - Sair")

    opcao: int = int(input("Digite a opção: "))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Volte Sempre!")
        sleep(2)
        exit(0)
    else:
        print("Valor incorreto. Opção invalida!")
        menu()


def criar_conta() -> None:
    """Cria a conta do cliente."""
    print("informe os dados do cliente: ")

    nome: str = input("Nome do cliente: ")
    email: str = input("E-mail do cliente: ")
    cpf: str = input("Cpf do cliente:")
    data_nascimento: str = input("Data de nascimento do cliente: ")

    # Instancia tanto o cliente quanto a conta do cliente.
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)  # insere a conta na nossa lista de contas

    print("Conta criada com sucesso.")
    print("\nDados da conta:")
    print(conta)
    menu()


def efetuar_saque() -> None:
    """Realiza o saque da conta."""
    if len(contas) > 0:  # se tiver contas cadastradas
        numero: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:  # Se a conta existe
            valor: float = float(input("Informe o valor do saque: "))
            conta.sacar(valor)  # A lógica do método irá estar aqui.
        else:
            print(f"Conta com número {numero} não foi localizada.")

    else:
        print("\nAinda não existem contas cadastradas.")
    sleep(0.5)
    menu()


def efetuar_deposito() -> None:
    """Realiza o depósito de alguma valor na conta."""
    if len(contas) > 0:  # se tiver contas cadastradas
        numero: int = int(input("Informe o número da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:  # Se a conta existe
            valor: float = float(input("Informe o valor do depósito: "))
            conta.depositar(valor)  # A lógica do método irá estar aqui.
        else:
            print(f"Conta com número {numero} não foi localizada.")
    else:
        print("\nAinda não existem contas cadastradas.")
    sleep(0.5)
    menu()


def efetuar_transferencia() -> None:
    """Realiza a transferência entre contas."""
    if len(contas) > 0:  # se tiver contas cadastradas
        numero: int = int(input("Informe o número da sua conta: "))

        conta_o: Conta = buscar_conta_por_numero(numero)  # conta de origem

        if conta_o:  # Se a conta existe
            numero_d: int = int(input("Digite o número da conta destino: "))
            conta_d: Conta = buscar_conta_por_numero(numero_d) # conta de destino

            if conta_d:
                valor: float = float(input("Informe o valor da transferência: "))
                conta_o.transferir(conta_d, valor)  # A lógica do método irá estar aqui.
                print("Valor transferido com sucesso!")
            else:
                print(f"Conta de destino {numero_d} não encontrada.")
        else:
            print(f"Conta com número {numero} não foi localizada.")
    else:
        print("\nAinda não existem contas cadastradas.")
    sleep(0.5)
    menu()


def listar_contas() -> None:
    """Lista as contas cadastradas."""
    if len(contas) > 0:
        print("\nListagem de contas:")

        for conta in contas:
            print(conta)
            print("------------------------")
            sleep(0.25)
    else:
        print("\nNão existem contas cadastradas")
    sleep(0.5)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
                break
    return c


if __name__ == "__main__":
    # Inicializo algumas coisas
    geremias: Cliente = Cliente('Geremias Corrêa', 'Geremias@gmail.com', \
    "123.456.789-43", "20/01/1997") 
    gabriela: Cliente = Cliente('Gabriela Rebello', 'Gabriela@gmail.com', \
    "124.156.389-43", "27/09/1998")
    contaf: Conta = Conta(geremias)
    contaa: Conta = Conta(gabriela)
    contas.append(contaf)
    contas.append(contaa)
    menu()