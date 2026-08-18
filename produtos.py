produtos_cadastrados = [{"nome": "Placa de vídeo", "categoria": "Informática", "preço": 4000, "estoque": 30}, ]

def cadastro_produtos():
    print("====================")
    print("Cadastro de produtos")
    print("====================")
    nome = input("Digite o nome do seu produto: ")
    categoria = input("Digite a categoria do seu produto: ")
    preco = input("Digite o preço do seu produto: ")
    estoque = ("Digite a quantidade disponível do seu produto: ")
    novo_produto = {"nome": nome, "categoria": categoria, "preço": preco, "estoque": estoque}
    produtos_cadastrados.append(novo_produto)
    print(f"O produto {nome} foi cadastrado com sucesso!")

def lista_produtos():
    for produto in produtos_cadastrados:
        print("Lista de produtos")
        print(f"{"Nome do produto".ljust(20)} | {"Categoria".ljust(20)} | {"Preço".ljust(20)} | {"Estoque"}")
        nome = produtos_cadastrados["nome"]
        categoria = produtos_cadastrados["categoria"]
        preco = produtos_cadastrados["preço"]
        estoque = produtos_cadastrados["estoque"]
        print(f"{nome.ljust(20)} | {categoria.ljust(20)} | {preco.ljust(20)} | {estoque}")

def busca_produto():
    print("Buscar produto")
    produto = input("Digite o nome do produto que quer procurar: ")
    for produto in produtos_cadastrados:
        if produto["nome"] in produtos_cadastrados:
            nome = produto["nome"]
            categoria = produto["categoria"]
            preco = produto["preço"]
            estoque = produto["estoque"]
            print(f"Nome: {nome}, Categoria: {categoria}, Preço: {preco}, Estoque: {estoque}")
        else:
            print("O produto não está na lista")