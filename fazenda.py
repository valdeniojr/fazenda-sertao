from dados import animais, produtos, metricas
from constantes import prefixos, tipos, animal_status

from utils import menu_opcoes, gerar_id, titulo, exibir_animais


def cadastrar_animal ():
	titulo("CADASTRAR ANIMAL")
	
	tipo_escolhido = menu_opcoes("Tipo de Animal", tipos, False)
	identificacao = gerar_id(prefixos, animais, tipo_escolhido)
	status_escolhido = menu_opcoes("Status do Animal", animal_status, False)
	
	animais.append({"tipo": tipo_escolhido, "identificacao": identificacao, "status": status_escolhido})
	print(f"Animal '{identificacao}' cadastrado com sucesso!")

def buscar_animal ():
	titulo("BUSCAR ANIMAL")
	while True:
		identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

		for animal in animais:
			if animal["identificacao"] == identificacao:
				exibir_animais(animal)
				break
		else:
			print("Nenhum animal com essa identificação foi encontrado.")

		nova_busca = input("Deseja realizar uma nova busca? (s/n): ").lower()

		if nova_busca != "s":
			break

def atualizar_animal():
	titulo("ATUALIZAR ANIMAL")

	while True:
		menu = ["Tipo", "Identificação", "Status"]
		campo = menu_opcoes("Qual informação deseja atualizar?", menu, True)

		if campo == 1:
			identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

			for animal in animais:
				if animal["identificacao"] == identificacao:
					tipo_escolhido = menu_opcoes("Tipo de Animal", tipos, False)
					animal["tipo"] = tipo_escolhido
					print(f"Animal '{animal["identificacao"]}' atualizado com sucesso!")
					break
			else:
				print("Nenhum animal com essa identificação foi encontrado.")
		elif campo == 2:
			identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

			for animal in animais:
				if animal["identificacao"] == identificacao:
					nova_identificacao = input("Informe a nova identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

					duplicado = True

					while duplicado:
						duplicado = False
						for animal in animais:
							if animal["identificacao"] == nova_identificacao:
								duplicado = True
								print(f"Identificação '{nova_identificacao}' já está em uso.")
								nova_identificacao = input("Informe a nova identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")
								break

					animal["identificacao"] = nova_identificacao
					print(f"Animal '{animal["identificacao"]}' atualizado com sucesso!")
					break
			else:
				print("Nenhum animal com essa identificação foi encontrado.")
		elif campo == 3:
			identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

			for animal in animais:
				if animal["identificacao"] == identificacao:
					status_escolhido = menu_opcoes("Status do Animal: ", animal_status, False)
					animal["status"] = status_escolhido
					print(f"Animal '{animal["identificacao"]}' atualizado com sucesso!")
					break
			else:
				print("Nenhum animal com essa identificação foi encontrado.")

		nova_alteracao = input("Deseja realizar uma nova alteração? (s/n): ").lower()

		if nova_alteracao != "s":
			break

def remover_animal():
	titulo("REMOVER ANIMAL")

	while True: 
		identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

		for i in range(len(animais)):
			animal = animais[i]

			if animal["identificacao"] == identificacao:
					exibir_animais(animal)

					confirmar_remocao = input("Tem certeza que deseja remover este animal? (s/n): ").lower()

					if confirmar_remocao != "n":
						animais.pop(i)	
						print("Animal removido com sucesso!")
					break
		else:
			print("Nenhum animal com essa identificação foi encontrado.")
		
		nova_remocao = input("Deseja realizar uma nova remoção? (s/n): ").lower()

		if nova_remocao != "s":
			break

def listar_animais():
	if len(animais) == 0:
		print("Nenhum animal cadastrado.")
	else:
		titulo("LISTA DE ANIMAIS")
		exibir_animais(animais)

		print(f"Total de Animais: {len(animais)}")

def producao_leite():
	titulo("PRODUÇÃO DE LEITE")

	litros = float(input("Informe a produção diária em litros: "))

	while litros < 0:
		print("Valor inválido. Tente novamente")

		litros = float(input("Informe a produção diária em litros: "))

	meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	mes = menu_opcoes("Produção Diária", meses, True)

	metricas[mes - 1]["producao"] += litros
	print(f"Produção de {litros}L registrada com sucesso!")

def cadastrar_produto():
	titulo("CADASTRAR PRODUTO")

	while True:
		nome_produto = input("Nome do produto: ")

		while nome_produto == "":
			print("Nome inválido. Tente novamente")
			nome_produto = input("Nome do produto: ")

		nome_duplicado = True

		while nome_duplicado: 
			nome_duplicado = False
			for produto in produtos:
				if produto["nome"] == nome_produto:
					print("Já existe um produto com esse nome. Tente novamente.")
					nome_produto = input("Nome do produto: ")
					nome_duplicado = True
					break

		kg = float(input("Peso do produto: "))

		while kg <= 0:
			print("Peso inválido. Tente novamente")
			kg = float(input("Peso do produto: "))

		preco = float(input("Preço do produto: "))

		produtos.append({"nome": nome_produto, "peso": kg, "estoque": 0, "preco": preco})
		print(f"Produto '{nome_produto}' cadastrado com sucesso!")

		novo_produto = input("Deseja cadastrar um novo produto? (s/n): ").lower()

		if novo_produto != "s":
			break

def adicionar_estoque():
	titulo("ADICIONAR ESTOQUE")

	while True:
		lista_produtos = []

		for produto in produtos:
			lista_produtos.append(produto["nome"])

		index = menu_opcoes("Lista de Produtos", lista_produtos, True)

		quantidade = int(input(f"Quantidade a adicionar em estoque para '{produtos[index - 1]["nome"]}': "))

		while quantidade < 0:
			print("Valor inválido. Tente novamente.")
			quantidade = int(input(f"Quantidade a adicionar em estoque para '{produtos[index - 1]["nome"]}': "))

		produtos[index - 1]["estoque"] += quantidade
		print(f"Estoque de '{produtos[index - 1]["nome"]}' atualizado com sucesso!")

		novo_estoque = input("Deseja atualizar o estoque de outro produto? (s/n): ").lower()

		if novo_estoque != "s":
			break