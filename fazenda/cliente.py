from database.dados import animais, produtos, lista_compras, lista_interesses, historico, agendamentos
from utils.utils import menu_opcoes, titulo, exibir_informacoes_endereco, exibir_produtos, exibir_animais, input_data, input_hora
from utils.helpers import clearCMD, buscar_endereco_por_cep, gerar_nota_fiscal
from fazenda.relatorio import registrar_movimentacao

from datetime import datetime

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
			lista_compras.append({"nome": produto["nome"], "quantidade": quantidade, "total": produto["preco"] * quantidade})
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

def comprar_animal():
	clearCMD()
	titulo("COMPRAR ANIMAL")

	while True:
		disponiveis = [a for a in animais if a["status"] == "Disponível p/ venda"]

		if not disponiveis:
			clearCMD()
			print("Nenhum animal disponível para venda.")
			return

		lista_animais = [f"{a['tipo']} - ({a['identificacao']})" for a in disponiveis]
		
		clearCMD()
		index = menu_opcoes("Escolha uma opção: ", lista_animais, True)
		animal = disponiveis[index - 1]

		print(f"Animal '{animal["identificacao"]}' adquirido com sucesso!")
		registrar_movimentacao("Compra", animal["identificacao"], 1)
		animais.remove(animal)
		lista_compras.append({"nome": animal["identificacao"], "tipo": animal["tipo"], "quantidade": 1, "total": 0})

		nova_compra = input("Deseja realizar outra compra? (s/n): ").lower()

		if nova_compra != "s":
			break

def agendar_retirada():
	clearCMD()
	titulo("AGENDAR RETIRADA")

	while True:
		if len(lista_compras) == 0:
			print("Nenhuma compra encontrada para agendar retirada.")
			break

		lista_produtos = [p["nome"] for p in lista_compras]
			
		clearCMD()
		index = menu_opcoes("Escolha o produto", lista_produtos, True)

		compra_selecionada = lista_compras[index - 1]

		cliente = input("Informe a razão social ou nome do cliente: ")

		data = input_data("Informe uma data para entrega (dd/mm/aaaa): ")
		hora = input_hora("Informe o horário para entrega (hh:mm): ")

		while True:
			cep = input("Informe o CEP para entrega (00000-000): ")

			data = buscar_endereco_por_cep(cep)

			clearCMD()

			if not data:
				print("CEP inválido ou API indisponível.")
				continue

			exibir_informacoes_endereco(data)

			confirmacao = input(f"Deseja realizar a entrega em {data.get('logradouro')}? (s/n): ").lower()

			if confirmacao == "s":
				break

		clearCMD()
		print("Retirada agendada com sucesso!")
		agendamentos.append({"data": data, "hora": hora, "item": compra_selecionada["nome"]})
		lista_compras.remove(compra_selecionada)

		gerar_nota_fiscal(cliente, data, compra_selecionada["nome"], compra_selecionada["quantidade"],compra_selecionada["total"])

		novo_agendamento = input("Deseja realizar outro agendamento? (s/n): ").lower()

		if novo_agendamento != "s":
			break

def registrar_interesse():
	clearCMD()
	titulo("REGISTRAR INTERESSE")

	while True:
		if not produtos:
			clearCMD()
			print("Nenhum produto disponível para compra.")
			return

		lista_nomes = [f"{p['nome']}" for p in produtos]
			
		clearCMD()
		index = menu_opcoes("Escolha o produto", lista_nomes, True)
		produto = produtos[index - 1]

		clearCMD()
		if produto in lista_interesses:
			print("Você já adicionou esse produto aos seus interesses.")
		else:
			lista_interesses.append(produto)
			print("Produto adicionado aos seus interesses com sucesso!")

		novo_interesse = input("Deseja adicionar outro produto aos seus interesses? (s/n): ")

		if novo_interesse != "s":
			break

def ver_interesses():
	clearCMD()
	titulo("MEUS INTERESSES")

	if not lista_interesses:
		print("Você ainda não demonstrou interesse em nenhum produto.")
		return
	
	lista_produtos = [p for p in produtos if p in lista_interesses]

	exibir_produtos(lista_produtos)