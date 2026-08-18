from produtos import produtos_cadastrados
regist_vendas = [{"nome": "Placa de vídeo", "Número de itens vendidos": 7, "Valor total da venda": 28000}, ]

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
                venda_produto = {"nome": nome, "Número de itens vendidos": num_vendas, "Valor total da venda": vlr_total}
                regist_vendas.append(venda_produto)
                print(f"O valor total das vendas do produto {nome} é de R${vlr_total}")

            else:
                print("Valor inválido, tente novamente")

    if not encontrado:
        print("O produto não foi encontrado na lista, tente novamente")