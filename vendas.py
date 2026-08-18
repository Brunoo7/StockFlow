from produtos import produtos_cadastrados
from main import voltar_menu
regist_vendas = [{"nome": "Placa de vídeo", "número de itens vendidos": 7, "valor total da venda": 28000}, ]

def registrar_venda():
    print("===============")
    print("Registrar venda")
    print("===============")
    nome_produto = input("Digite o nome do produto vendido: ")
    encontrado = False
    for produto in produtos_cadastrados:

        if nome_produto == produto["nome"]:
            encontrado = True
            num_vendas = int(input("Digite a quantidade de itens vendidos: "))
            nome = produto["nome"]
            preco = produto["preço"]

            if num_vendas <= produto["estoque"]:
                produto["estoque"] -= num_vendas
                vlr_total = num_vendas * preco
                venda_produto = {"nome": nome, "número de itens vendidos": num_vendas, "valor total da venda": vlr_total}
                regist_vendas.append(venda_produto)
                print(f"O valor total das vendas do produto {nome} é de R${vlr_total}")

            else:
                print("Valor inválido, tente novamente")

    if not encontrado:
        print("O produto não foi encontrado na lista, tente novamente")
    voltar_menu()

def listar_vendas():
    print("======")
    print("Vendas")
    print("======")
    print(f"{"Nome do produto".ljust(20)} | {"Número de itens vendidos".ljust(20)} | {"Valor total da venda"}")
    for produto in regist_vendas:
        nome = produto["nome"]
        num_itens = produto["número de itens vendidos"]
        vlr_total = produto["valor total da venda"]
        print(f"{nome.ljust(20)} | {str(num_itens).ljust(20)} | {vlr_total} ")
    voltar_menu()

def mostrar_faturamento():
    print("=================")
    print("Faturamento total")
    print("=================")
    faturamento_total = 0
    for produto in regist_vendas:
        nome = produto["nome"]
        vlr_total = produto["valor total da venda"]
        faturamento_total = faturamento_total + vlr_total
        print(f"O produto {nome} teve o faturamento de R${vlr_total}")
    print(f"O faturamento total é de R${faturamento_total}")
    voltar_menu()
