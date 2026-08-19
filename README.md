#  StockFlow — Sistema de Estoque e Vendas

Sistema de gerenciamento de **estoque e vendas** desenvolvido em Python para uma pequena loja.

O projeto permite cadastrar produtos, controlar o estoque, registrar vendas e gerar relatórios com informações sobre os produtos e o faturamento.

##  Funcionalidades

* **Cadastrar produtos**

  * Nome
  * Categoria
  * Preço
  * Quantidade em estoque

* **Listar produtos**

  * Exibe todos os produtos cadastrados e suas informações.

* **Buscar produto**

  * Pesquisa um produto pelo nome.
  * Informa quando o produto não está cadastrado.

* **Atualizar estoque**

  * Adicionar unidades ao estoque.
  * Retirar unidades do estoque.
  * Impede que o estoque fique negativo.

* **Registrar vendas**

  * Seleciona o produto vendido.
  * Define a quantidade vendida.
  * Verifica se existe estoque suficiente.
  * Atualiza automaticamente o estoque.
  * Calcula o valor total da venda.

* **Listar vendas**

  * Exibe os produtos vendidos.
  * Quantidade de itens vendidos.
  * Valor total de cada venda.

* **Mostrar faturamento**

  * Exibe o faturamento de cada produto.
  * Calcula o faturamento total.

* **Mostrar relatório**

  * Quantidade de produtos cadastrados.
  * Quantidade de produtos sem estoque.
  * Produto com maior quantidade em estoque.
  * Produto mais vendido.
  * Faturamento total.

##  Tecnologias utilizadas

* **Python 3**
* Listas
* Dicionários
* Funções
* Estruturas de repetição `for` e `while`
* Estruturas condicionais `if`, `elif` e `else`
* `match/case`
* Módulos Python
* Terminal/Console

##  Estrutura do projeto

```text
StockFlow/
│
├── main.py
├── produtos.py
└── vendas.py
```

### `main.py`

Responsável pelo funcionamento principal do sistema:

* Menu interativo
* Controle das opções
* Relatórios
* Faturamento total
* Encerramento do programa

### `produtos.py`

Responsável pelo gerenciamento dos produtos:

* Cadastro
* Listagem
* Busca
* Atualização do estoque

Os produtos são armazenados na lista `produtos_cadastrados`.

### `vendas.py`

Responsável pelo gerenciamento das vendas:

* Registro de vendas
* Atualização do estoque após uma venda
* Listagem das vendas
* Cálculo do faturamento

As vendas são armazenadas na lista `regist_vendas`.

## ▶️ Como executar

1. Tenha o **Python 3** instalado.

2. Clone ou baixe este repositório.

3. Abra o terminal na pasta do projeto.

4. Execute:

```bash
python main.py
```

5. Utilize o menu para navegar pelo sistema.

##  Menu

```text
======================================
StockFlow: Sistema de Estoque e Vendas
======================================

1- Cadastro de produtos
2- Lista de produtos cadastrados
3- Buscar produto
4- Atualizar estoque
5- Registrar vendas
6- Listar vendas
7- Mostrar faturamento
8- Mostrar relatório
9- Sair
```

##  Armazenamento dos dados

Os dados são armazenados em **listas de dicionários** durante a execução do programa.

### Exemplo de produto

```python
{
    "nome": "Placa de vídeo",
    "categoria": "Informática",
    "preço": 4000,
    "estoque": 30
}
```

### Exemplo de venda

```python
{
    "nome": "Placa de vídeo",
    "número de itens vendidos": 7,
    "valor total da venda": 28000
}
```

##  Objetivo do projeto

O StockFlow foi desenvolvido com o objetivo de aplicar conceitos fundamentais de programação em Python, incluindo **funções, listas, dicionários, estruturas de repetição, estruturas condicionais e organização do código em diferentes módulos**.

---

**StockFlow — Sistema de Estoque e Vendas**
Desenvolvido em Python.
