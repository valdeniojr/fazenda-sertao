from database.dados import animais, produtos, lista_compras, lista_interesses, historico
from utils.utils import menu_opcoes, titulo, exibir_produtos, exibir_animais, clearCMD
from fazenda.relatorio import registrar_movimentacao

def ver_estoque():
	clearCMD()
	titulo("ESTOQUE DISPONÍVEL")

	menu = ["Estoque de Animais", "Estoque de Produtos"]
	tipo_estoque = menu_opcoes("Qual estoque deseja visualizar?", menu, True)

	if tipo_estoque == 1:
		if len(animais) == 0:
			clearCMD()
			print("Nenhum animal cadastrado.")
		else:
			clearCMD()
			titulo("ESTOQUE DE ANIMAIS")
			exibir_animais(animais)
			print(f"Total de Animais: {len(animais)}")
	else:
		if len(produtos) == 0:
			clearCMD()
			print("Nenhum produto cadastrado.")
		else:
			clearCMD()
			titulo("ESTOQUE DE PRODUTOS")
			exibir_produtos(produtos)
			print(f"Total de Produtos: {len(produtos)}")

def comprar_produto():
	clearCMD()
	titulo("COMPRAR PRODUTO")

	while True:
		menu = ["Ver todos os produtos", "Escolher da minha lista de interesses"]
		origem = menu_opcoes("De onde deseja escolher o produto?", menu, True)

		if origem == 1:
			disponiveis = [p for p in produtos if p["estoque"] > 0]

			if not disponiveis:
				clearCMD()
				print("Nenhum produto disponível para compra.")
				return

			lista_nomes = [f"{p['nome']} - R$ {p['preco']:.2f}" for p in disponiveis]
			
			clearCMD()
			index = menu_opcoes("Escolha o produto", lista_nomes, True)
			produto = disponiveis[index - 1]

			quantidade = int(input(f"Quantas unidades de '{produto['nome']}' deseja comprar? "))

			while quantidade <= 0 or quantidade > produto["estoque"]:
				clearCMD()
				print(f"Quantidade inválida. Disponível: {produto['estoque']} unidade(s).")
				quantidade = int(input(f"Quantas unidades de '{produto['nome']}' deseja comprar? "))

			produto["estoque"] -= quantidade
			lista_compras.append({"produto": produto["nome"], "quantidade": quantidade, "total": produto["preco"] * quantidade})
			registrar_movimentacao("Compra", produto["nome"], quantidade)
			clearCMD()
			print(f"Compra de {quantidade}x '{produto['nome']}' realizada! Total: R$ {produto['preco'] * quantidade:.2f}")
		else:
			nomes_interesse = {i["produto"] for i in lista_interesses}
			disponiveis = [p for p in produtos if p["nome"] in nomes_interesse and p["estoque"] > 0]

			if len(lista_interesses) == 0:
				clearCMD()
				print("Você ainda não demonstrou interesse em nenhum produto.")
				break

			if not disponiveis:
				clearCMD()
				print("Nenhum produto de interesse está disponível no momento.")
				return

			lista_nomes = [f"{p['nome']} - R$ {p['preco']:.2f}" for p in disponiveis]

			clearCMD()
			index = menu_opcoes("Escolha o produto", lista_nomes, True)
			produto = disponiveis[index - 1]

			quantidade = int(input(f"Quantas unidades de '{produto['nome']}' deseja comprar? "))

			while quantidade <= 0 or quantidade > produto["estoque"]:
				clearCMD()
				print(f"Quantidade inválida. Disponível: {produto['estoque']} unidade(s).")
				quantidade = int(input(f"Quantas unidades de '{produto['nome']}' deseja comprar? "))

			produto["estoque"] -= quantidade
			lista_compras.append({"produto": produto["nome"], "quantidade": quantidade, "total": produto["preco"] * quantidade})
			registrar_movimentacao("Compra", produto["nome"], quantidade)
			clearCMD()
			print(f"Compra de {quantidade}x '{produto['nome']}' realizada! Total: R$ {produto['preco'] * quantidade:.2f}")

		nova_compra = input("Deseja realizar outra compra? (s/n): ").lower()

		if nova_compra != "s":
			break

