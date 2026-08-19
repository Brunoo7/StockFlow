from produtos import cadastro_produtos, lista_produtos, busca_produto, atualizar_estoque, produtos_cadastrados
from vendas import registrar_venda, listar_vendas, mostrar_faturamento, regist_vendas
import os 

def sair():
    print("Fechando programa...")
    os.system("cls")

def quantidade_registrados():
    quantidade_produtos = 0
    for produto in produtos_cadastrados:
        quantidade_produtos += 1
    print(f"Quantidade de produtos cadastrados {quantidade_produtos}")

def quantidade_sem_estoque():
    sem_estoque = 0
    for produto in produtos_cadastrados:
        estoque = produto["estoque"]
    
        if estoque == 0:
            sem_estoque += 1
    print(f"Quantidade de produtos sem estoque {sem_estoque}")

def produto_maior_estoque():
    maior_estoque = 0
    produto_estoque = ""
    for produto in produtos_cadastrados:
        estoque = produto["estoque"]

        if estoque > maior_estoque:
            produto_estoque = produto["nome"]
            maior_estoque = produto["estoque"]
    print(f"O produto {produto_estoque} tem o maior estoque com {maior_estoque} itens")

def produto_mais_vendido():
    maior_venda = 0
    produto_maior_venda = ""
    venda_por_produto = {}
    for venda in regist_vendas:
        nome = venda["nome"]
        ven = venda["número de itens vendidos"]
        if nome not in venda_por_produto:
            venda_por_produto[nome] = ven
        else:
            venda_por_produto[nome] += ven
    for venda in venda_por_produto:
        if maior_venda < venda_por_produto[venda]:
            produto_maior_venda = venda
            maior_venda = venda_por_produto[venda]

    print(f"Produto {produto_maior_venda} é o mais vendido com {maior_venda} vendas")

def fatur_total():
    faturamento_total = 0
    for produto in regist_vendas:
        vlr_total = produto["valor total da venda"]
        faturamento_total = faturamento_total + vlr_total

    print(f"Faturamento total {faturamento_total}")

def mostrar_relatorio():
    quantidade_registrados()
    quantidade_sem_estoque()
    produto_maior_estoque()
    produto_mais_vendido()
    fatur_total()

def opcoes():
    print("1- Cadastro de produtos")
    print("2- Lista de produtos cadastrados")
    print("3- Buscar produto")
    print("4- Atualizar estoque")
    print("5- Registrar vendas")
    print("6- Listar vendas")
    print("7- Mostrar faturamento")
    print("8- Mostrar relatório")
    print("9- Sair")

def menu():
    print("======================================")
    print("StockFlow: Sistema de Estoque e Vendas")
    print("======================================")
    opcao = 0
    while opcao != 9:
        opcoes()
        try:
            opcao = int(input("Escolha uma opção: "))
            match opcao:
                case 1:
                    cadastro_produtos()
                case 2:
                    lista_produtos()
                case 3:
                    busca_produto()
                case 4:
                    atualizar_estoque()
                case 5:
                    registrar_venda()
                case 6:
                    listar_vendas()
                case 7:
                    mostrar_faturamento()
                case 8:
                    mostrar_relatorio()
                case 9:
                    sair()
                case _:
                    print("Opção inválida, tente novamente")
        except ValueError:
            print("Opção inválida, tente novamente")

menu()