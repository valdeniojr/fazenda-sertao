usuarios = [
	["johndoe", "12345", True], # Usuário teste
	["janedoe", "12345", False] # Usuário teste
]

animais = [
	["Ovino", "2232", "Para engorda"]
]

metricas = [
	["Jan", 0.0],
	["Fev", 0.0],
	["Mar", 0.0],
	["Abr", 0.0],
	["Maio", 0.0],
	["Jun", 0.0],
	["Jul", 0.0],
	["Ago", 0.0],
	["Set", 0.0],
	["Out", 0.0],
	["Nov", 0.0],
	["Dez", 0.0],
]

produtos = [
	["Queijo Coalho", 10.0, 100], # Item teste
	["Queijo Manteiga", 10.0, 100], # Item teste
	["Queijo", 10.0, 100], # Item teste
]

logado = False
admin = False

while not logado:
	usuario = input("Digite seu usuário: ")
	senha = input("Digite sua senha: ")

	for user in usuarios:
		if user[0] == usuario and user[1] == senha:
			logado = True
			print("Login realizado com sucesso!")
			if user[2]:
				admin = user[2]
			break
	else:
		print("As credenciais informadas não existem.")

while True:
	if admin:
		print("=" * 40)
		print("          MENU DO ADMINISTRADOR          ")
		print("=" * 40)

		print("")

		print("1 - Cadastrar Animal")
		print("2 - Buscar Animal")
		print("3 - Atualizar Animal")
		print("4 - Remover Animal")
		print("5 - Listar Animais")

		print("")

		print("6 - Registrar Produção de Leite")
		print("7 - Criar Produto")
		print("8 - Adicionar Produto ao Estoque")
		print("9 - Ver Estoque Atual")
		print("10 - Gráfico de Produção de Leite")

		print("")

		op = int(input("Escolha uma opção: "))

		if op == 1:
			print("=" * 40)
			print("          CADASTRAR ANIMAL          ")
			print("=" * 40)

			while True:
				print("Tipo de Animal: ")
				print("1 - Bovino de Leite")
				print("2 - Caprino")
				print("3 - Ovino")
				print("4 - Suíno")
				
				tipo = int(input("Escolha (1-4): "))

				if tipo in (1, 2, 3, 4):
					break
				else:
					print("Opção inválida. Tente novamente.")

			indentificacao = input("Identificação (brinco ou número único): ")

			while True:
				print("Status do Animal: ")
				print("1 - Em lactação")
				print("2 - Para engorda")
				print("3 - Disponível p/ venda")

				status = int(input("Escolha (1-3): "))

				if status in (1, 2, 3):
					break
				else:
					print("Opção inválida. Tente novamente.")

			duplicado = False

			for animal in animais:
				if animal[1] == indentificacao:
					print("Já possui um animal com essa identificação.")
					duplicado = True
					break

			if not duplicado: 
				if tipo == 1:
					tipo = "Bovino de Leite"
				elif tipo == 2:
					tipo = "Caprino"
				elif tipo == 3:
					tipo = "Ovino"
				elif tipo == 4:
					tipo = "Suíno"

				if status == 1:
					status = "Em lactação"
				elif status == 2:
					status = "Para engorda"
				elif status == 3:
					status = "Disponível p/ venda"

				animais.append([tipo, indentificacao, status])
				print(f"Animal de identificação ({indentificacao}) cadastrado com sucesso.")
		elif op == 2:
			print("=" * 40)
			print("          BUSCAR ANIMAL          ")
			print("=" * 40)

			while True:
				indentificacao = input("Identificação (brinco ou número único): ")

				for animal in animais:
					if animal[1] == indentificacao:
						print("========== RESULTADO DA BUSCA ==========")
						print(f"Tipo: {animal[0]}")
						print(f"Identificação: {animal[1]}")
						print(f"Status: {animal[2]}")
						print("=" * 40)
						break
				else:
					print("Animal não encontrado.")

				nova_busca = input("Deseja realizar uma nova busca? (s/n): ").lower()

				if nova_busca != "s":
					break
		elif op == 3:
			print("=" * 40)
			print("          ATUALIZAR ANIMAL          ")
			print("=" * 40)

			while True:
				while True:
					print("Qual informação deseja atualizar?")
					print("1 - Tipo")
					print("2 - Identificação")
					print("3 - Status")

					op = int(input("Escolha (1-3): "))

					if op in (1, 2, 3):
						break
					else:
						print("Opção inválida. Tente novamente.")

				if op == 1:
					indentificacao = input("Identificação (brinco ou número único): ")

					for animal in animais:
						if animal[1] == indentificacao:
							while True:
								print("Tipo de Animal: ")
								print("1 - Bovino de Leite")
								print("2 - Caprino")
								print("3 - Ovino")
								print("4 - Suíno")

								tipo = int(input("Escolha (1-4): "))

								if tipo in (1, 2, 3, 4):
									break
								else:
									print("Opção inválida. Tente novamente.")

							if tipo == 1:
								tipo = "Bovino de Leite"
							elif tipo == 2:
								tipo = "Caprino"
							elif tipo == 3:
								tipo = "Ovino"
							elif tipo == 4:
								tipo = "Suíno"

							animal[0] = tipo
							print(f"Animal ({animal[1]}) atualizado com sucesso!")
							break
					else:
						print("Animal não encontrado.")
				elif op == 2:
					indentificacao = input("Identificação (brinco ou número único): ")

					for animal in animais:
						if animal[1] == indentificacao:
							nova_identificacao = input("Nova identificação (brinco ou número único): ")

							animal[1] = nova_identificacao
							print(f"Animal ({animal[1]}) atualizado com sucesso!")
							break
					else:
						print("Animal não encontrado.")
				elif op == 3:
					indentificacao = input("Identificação (brinco ou número único): ")

					for animal in animais:
						if animal[1] == indentificacao:
							while True:
								print("Status do Animal: ")
								print("1 - Em lactação")
								print("2 - Para engorda")
								print("3 - Disponível p/ venda")

								status = int(input("Escolha (1-3): "))

								if status in (1, 2, 3):
									break
								else:
									print("Opção inválida. Tente novamente.")

							if status == 1:
								status = "Em lactação"
							elif status == 2:
								status = "Para engorda"
							elif status == 3:
								status = "Disponível p/ venda"

							animal[2] = status
							print(f"Animal ({animal[1]}) atualizado com sucesso!")
							break

				nova_alteracao = input("Deseja realizar uma nova alteração? (s/n): ").lower()

				if nova_alteracao != "s":
					break
		elif op == 4:
			print("=" * 40)
			print("          REMOVER ANIMAL          ")
			print("=" * 40)

			while True: 
				indentificacao = input("Identificação (brinco ou número único): ")

				for i in range(len(animais)):
					animal = animais[i]

					if animal[1] == indentificacao:
							print("========== DETALHES DO ANIMAL ==========")
							print(f"Tipo: {animal[0]}")
							print(f"Identificação: {animal[1]}")
							print(f"Status: {animal[2]}")
							print("=" * 40)

							confirmar_remocao = input("Tem certeza que deseja remover este animal? (s/n): ").lower()

							if confirmar_remocao != "n":
								animais.pop(i)	
								print("Animal removido com sucesso.")
							break
				else:
					print("Animal não encontrado.")
				
				nova_remocao = input("Deseja realizar uma nova remoção? (s/n): ").lower()
	
				if nova_remocao != "s":
					break
		elif op == 5:
			if len(animais) == 0:
				print("Não possui nenhum animal cadastrado.")
			else:
				print("=" * 40)
				print(f"{"TIPO":<15} {"BRINCO":<10} {"STATUS":<13}")
				print("=" * 40)
	
				for animal in animais:
					print(f"{animal[0]:<15} {animal[1]:<10} {animal[2]:<13}")
	
				print("=" * 40)
				print(f"Total de Animais: {len(animais)}")
		elif op == 6:
			print("=" * 40)
			print("          PRODUÇÃO DE LEITE          ")
			print("=" * 40)

			litro = float(input("Registre a produção diária: "))

			while litro < 0:
				print("Insira um valor válido.")

				litro = float(input("Registre a produção diária: "))

			while True:
				print("Informe o mês atual:")
				print("1 - Janeiro")
				print("2 - Fevereiro")
				print("3 - Março")
				print("4 - Abril")
				print("5 - Maio")
				print("6 - Junho")
				print("7 - Julho")
				print("8 - Agosto")
				print("9 - Setembro")
				print("10 - Outubro")
				print("11 - Novembro")
				print("12 - Dezembro")

				mes = int(input("Escolha (1-12): "))

				if mes in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
					break
				else:
					print("Opção inválida. Tente Novamente")

			for i in range(len(metricas)):
				metrica = metricas[i]
				if i == (mes - 1):
					metrica[1] += litro
					break

			print(f"Produção diária de leite registrada com sucesso.")
		elif op == 7:
			print("=" * 40)
			print("          CRIAR PRODUTO          ")
			print("=" * 40)

			nome_produto = input("Informe o nome do produto: ")

			while nome_produto == "":
				print("Nome inválido. Tente novamente")
				nome_produto = input("Informe o nome do produto: ")

			for produto in produtos:
				if produto[0] == nome_produto:
					print("Já existe um produto com esse nome. Tente novamente.")
					nome_produto = input("Informe o nome do produto: ")
					break

			kg = float(input("Informe o peso do produto: "))

			while kg <= 0:
				print("Peso inválido. Tente novamente")
				kg = float(input("Informe o peso do produto: "))

			produtos.append([nome_produto, kg, 0])
			print(f"O Produto {nome_produto} foi criado com sucesso.")
		elif op == 8:
			print("=" * 40)
			print("          ADICIONAR ESTOQUE          ")
			print("=" * 40)

			print("")

			while True:
				while True:
				
					print("Escolha um produto: ")
					for i in range(len(produtos)):
						produto = produtos[i]

						print(f"{i + 1} - {produto[0]}")

					print("")

					op = int(input("Escolha um produto: "))
					
					if op >= 0:
						break

				quantidade = int(input(f"Informe a quantidade que deseja adicionar ao estoque para o produto {produtos[op - 1][0]}: "))

				while quantidade < 0:
					print("Valor inválido. Tente novamente.")
					quantidade = int(input(f"Informe a quantidade que deseja adicionar ao estoque para o produto {produtos[op- 1][0]}: "))

				produtos[op - 1][2] += quantidade
				print(f"O Estoque do produto {produtos[op - 1][0]} foram adicionados com sucesso.")
				print(produtos)

				nova_estoque = input("Deseja adicionar estoque em mais algum produto? (s/n): ").lower()

				if nova_estoque != "s":
					break
	else:
		print("=" * 40)
		print("          MENU DO CLIENTE          ")
		print("=" * 40)

		print("")

		print("1 - Ver Estoque Disponível")
		print("2 - Comprar Produto")
		print("3 - Comprar Animal")
		print("4 - Agendar Retirada")
		print("5 - Registrar Interesse em Produto")
		print("6 - Ver Meus Interesses")

		print("")

		op = int(input("Escolha uma opção: "))