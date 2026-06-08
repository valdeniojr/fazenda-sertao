from database.dados import produtos
from utils.utils import menu_opcoes, titulo, exibir_produtos
from utils.helpers import clearCMD
from fazenda.relatorio import registrar_movimentacao

def cadastrar_produto():
	clearCMD()
	titulo("CADASTRAR PRODUTO")

	while True:
		nome_produto = input("Nome do produto: ")

		while nome_produto == "":
			clearCMD()
			print("Nome inválido. Tente novamente")
			nome_produto = input("Nome do produto: ")

		nome_duplicado = [p for p in produtos if p["nome"].lower() == nome_produto.lower()]

		while nome_duplicado:
			clearCMD()
			print("Já existe um produto com esse nome. Tente novamente.")
			nome_produto = input("Nome do produto: ")
			
			nome_duplicado = [p for p in produtos if p["nome"].lower() == nome_produto.lower()]

		kg = float(input("Peso do produto: "))

		while kg <= 0:
			clearCMD()
			print("Peso inválido. Tente novamente")
			kg = float(input("Peso do produto: "))

		preco = float(input("Preço do produto: "))

		produtos.append({"nome": nome_produto, "peso": kg, "estoque": 0, "preco": preco})
		registrar_movimentacao("Cadastro", nome_produto, 0)
		clearCMD()
		print(f"Produto '{nome_produto}' cadastrado com sucesso!")

		novo_produto = input("Deseja cadastrar um novo produto? (s/n): ").lower()

		if novo_produto != "s":
			clearCMD()
			break

def adicionar_estoque():
	clearCMD()
	titulo("ADICIONAR ESTOQUE")

	while True:
		lista_nomes = [produto["nome"] for produto in produtos]

		index = menu_opcoes("Lista de Produtos", lista_nomes, True)

		quantidade = int(input(f"Quantidade a adicionar em estoque para '{produtos[index - 1]['nome']}': "))

		while quantidade < 0:
			clearCMD()
			print("Valor inválido. Tente novamente.")
			quantidade = int(input(f"Quantidade a adicionar em estoque para '{produtos[index - 1]['nome']}': "))

		produtos[index - 1]["estoque"] += quantidade
		registrar_movimentacao("Entrada", produtos[index - 1]['nome'], quantidade)
		clearCMD()
		print(f"Estoque de '{produtos[index - 1]['nome']}' atualizado com sucesso!")

		novo_estoque = input("Deseja atualizar o estoque de outro produto? (s/n): ").lower()

		if novo_estoque != "s":
			clearCMD()
			break

def listar_produtos():
	clearCMD()
	if len(produtos) == 0:
		print("Nenhum produto cadastrado.")
	else:
		titulo("LISTA DE PRODUTOS")
		exibir_produtos(produtos)
		print(f"Total de Produtos: {len(produtos)}")
