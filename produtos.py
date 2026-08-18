from main import voltar_menu
produtos_cadastrados = [{"nome": "Placa de vídeo", "categoria": "Informática", "preço": 4000, "estoque": 30}, ]

def cadastro_produtos():
    print("====================")
    print("Cadastro de produtos")
    print("====================")
    nome = input("Digite o nome do seu produto: ")
    categoria = input("Digite a categoria do seu produto: ")
    preco = int(input("Digite o preço do seu produto: "))
    estoque = int(input("Digite a quantidade disponível do seu produto: "))
    novo_produto = {"nome": nome, "categoria": categoria, "preço": preco, "estoque": estoque}
    produtos_cadastrados.append(novo_produto)
    print(f"O produto {nome} foi cadastrado com sucesso!")
    voltar_menu()

def lista_produtos():
    print("=================")
    print("Lista de produtos")
    print("=================")
    print(f"{"Nome do produto".ljust(20)} | {"Categoria".ljust(20)} | {"Preço".ljust(20)} | {"Estoque"}")
    for produto in produtos_cadastrados:
        nome = produto["nome"]
        categoria = produto["categoria"]
        preco = produto["preço"]
        estoque = produto["estoque"]
        print(f"{nome.ljust(20)} | {categoria.ljust(20)} | {str(preco).ljust(20)} | {estoque}")
    voltar_menu()

def busca_produto():
    print("==============")
    print("Buscar produto")
    print("==============")
    nome_produto = input("Digite o nome do produto que quer procurar: ")
    encontrado = False
    for produto in produtos_cadastrados:

        if nome_produto == produto["nome"]:
            encontrado = True
            nome = produto["nome"]
            categoria = produto["categoria"]
            preco = produto["preço"]
            estoque = produto["estoque"]
            print(f"Nome: {nome}, Categoria: {categoria}, Preço: {preco}, Estoque: {estoque}")

    if not encontrado:
        print("O produto não está cadastrado")
    voltar_menu()

def atualizar_estoque():
    print("=================")
    print("Atualizar estoque")
    print("=================")
    nome_produto = input("Digite o nome do produto que deseja mudar no estoque: ")

    encontrado = False

    for produto in produtos_cadastrados:

        if nome_produto == produto["nome"]:
            encontrado = True
            nome = produto["nome"]
            estoque = produto["estoque"]
            print(f"Nome: {nome}, Estoque: {estoque}")
            mud = input("Deseja adicionar ou retirar itens do estoque?")

            if mud == "adicionar":
                qnt = int(input("Quantos itens deseja adicionar ao estoque?"))
                produto["estoque"] += qnt
                print(f"Nome: {nome}, Estoque: {produto['estoque']}")
                print("Estoque atualizado com sucesso!")

            elif mud == "retirar":
                qnt = int(input("Quantos itens deseja retirar do estoque?"))
                if qnt <= produto["estoque"]:
                    produto["estoque"] -= qnt
                    print(f"Nome: {nome}, Estoque: {produto['estoque']}")
                    print("Estoque atualizado com sucesso!")
                else:
                    print("Valor inválido, tente novamente")
            else:
                print("Erro, tente novamente")

    if not encontrado:
            print("O produto não está cadastrado")  
    voltar_menu()