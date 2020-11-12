from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

# Os produtos são uma lista de produtos (classe).
produtos: List[Produto] = []

# O Carrinho é um dict, pq é o produto e a qtd de produtos
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print("\n###################################")
    print("############ BEM-VINDO ############")
    print("############ SHOPTIME #############")
    print("###################################")
    print("\nSelecione uma opção abaixo: ")
    print("[1] - Cadastrar produto")
    print("[2] - Listar produtos")
    print("[3] - Comprar produto")
    print("[4] - Visualizar carrinho")
    print("[5] - Fechar pedido")
    print("[6] - Sair")

    opcao: int = int(input("Digite aqui: "))

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print("Volte sempre!")
        sleep(2)  # Dorme por 2 seg e sai.
        exit(0)
    else:
        sleep(1)
        print("Opção inválida.")
        menu()

def cadastrar_produto() -> None:
    print("\n###################################")
    print("###### Cadastro de produto ########\n")
    
    nome: str = input("Informe o nome do produto: ")
    preco: float = input("Informe o preço do produto: ")

    produto: Produto = Produto(nome, preco)
    produtos.append(produto)

    print(f"O produto {produto.nome} foi cadastrado com sucesso!")
    sleep(1)
    menu()

def listar_produtos() -> None:
    if len(produtos) > 0:
        print("########## Listagem de produtos ########")
        for produto in produtos:
            print(produto, "\n")
            sleep(0.5)
    else:
        print("Ainda não existem produtos cadastrados.")
    sleep(1)
    menu()


def comprar_produto() -> None:
    """Função de compra do produto, é a mais complexa."""
    if len(produtos) > 0:
        # Não tem sentido comprar um produto se eles não existem
        # print("Informe o código do produto: ")
        for produto in produtos:
            print(produto)
            print("-----------------------------")
            sleep(0.5)
        codigo: int = int(input("Digite o código do produto: "))

        produto: Produto = pega_produto_por_codigo(codigo)
        if produto:  # Dif de None
            # Se o carrinho é diferente de zero, precisamos verificar se ele está inserido
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quantidade: int = item.get(produto)  # se encontrar a chave, devolve o valor
                    # Se a quantidade em questão do produto procurado é 1 ou maior
                    if quantidade:  # se diferente de 0 a qtd dele no carrinho
                        item[produto] = quantidade + 1
                        print(
                            f"O produto {produto.nome} agora possui "
                            f"{quantidade + 1} unidades no carrinho."
                            )
                        tem_no_carrinho = True
                        sleep(1)
                        menu()
                    else:
                        pass
                # Se tem produtos no carrinho mas não o produto em questão
                if not tem_no_carrinho:  # Só chega aqui se não entrar no if de qtd
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                    sleep(1)
                    menu()
            else:
                item = {produto: 1}  # adc 1 produto
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                sleep(1)
                menu()
        else:
            print(f"O produto não foi encontrado.")
        sleep(1)
    else:
        print("Não há produtos cadastrados no sistema.")
    sleep(1)
    menu()

def visualizar_carrinho() -> None:
    """Visualiza o carrinho."""
    if len(carrinho) > 0:
        print("\nProdutos do carrinho: ")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])  # dados[0] = Produto (produto em si)
                print(f"Quantidade: {dados[1]}")  # dados[1] = int (quantidade)
                print("------------------------")
                sleep(0.5)
                """ Obs: dados[0] e [1] pois temos que um carrinho é um dict
                de Produto e inteiro (qtd), para cada um desses itens (item)
                no carrinho, então teremos no for de dados o dados[0] como
                o Produto(classe) em si e o dados[1] a sua quantidade.
                """
    else:
        print("Ainda não existem produtos no carrinho.")
    sleep(1)
    menu()


def fechar_pedido() -> None:
    """Fecha o pedido do cliente."""
    if len(carrinho) > 0:
        valor_total: float = 0
        print("######## Produtos do carrinho ########")
        for item in carrinho:  
            for dados in item.items():  # conjunto de chave valor
                print(dados[0])  # dados do produto classe
                print(f"Quantidade: {dados[1]}")  # quantidade de produtos
                print(dados[1])
                print(dados[0].preco)
                valor_total += float(dados[0].preco) * int(dados[1])  # preco * qtd
                # Obs: se não converter pra float o .preco, ele entende como str.
                sleep(0.5)
        # print(f"Sua fatura é {formata_float_str_moeda(valor_total)}")
        print(f"Sua fatura é de R$ {valor_total}.")
        print("Volte sempre!")
        carrinho.clear()
        sleep(2)
    else:
        print("Ainda não existem produtos no carrinho. Não há com fechar o pedido.")
    sleep(1)


def pega_produto_por_codigo(codigo: int) -> None:
    """Itera sobre os produtos para verificar se um bate com o parâmetro."""
    p: Produto = None  # do tipo None, para inicializar vazia

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == "__main__":
    main()

