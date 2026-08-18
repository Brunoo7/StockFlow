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