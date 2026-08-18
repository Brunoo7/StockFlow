from produtos import cadastro_produtos, lista_produtos, busca_produto, atualizar_estoque
from vendas import registrar_venda, listar_vendas, mostrar_faturamento
import os 

def voltar_menu():
    input("Selecione uma tecla para voltar ao menu principal: ")
    menu()

def sair():
    print("Fechando programa...")
    os.system("cls")
    menu()

def mostrar_relatorio():

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
    except:
        print("Opção inválida, tente novamente")