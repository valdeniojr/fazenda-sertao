usuarios = [
	["johndoe", "12345", True],
	["janedoe", "12345", False]
]

animais = []

metricas = [
	["Jan", 0],
	["Fev", 0],
	["Mar", 0],
	["Abr", 0],
	["Mai", 0],
	["Jun", 0],
	["Jul", 0],
	["Ago", 0],
	["Set", 0],
	["Out", 0],
	["Nov", 0],
	["Dez", 0],
]

produtos = []
lista_compras = []
agendamentos = []
lista_interesses = []

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
		print("11 - Cadastrar Usuário")
		print("12 - Sair")

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

			identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

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
				print(f"Animal '{identificacao}' cadastrado com sucesso!")
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

			litro = int(input("Registre a produção diária: "))

			while litro < 0:
				print("Insira um valor válido.")

				litro = int(input("Registre a produção diária: "))

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

			print("")

			while True:
				nome_produto = input("Informe o nome do produto: ")

				while nome_produto == "":
					print("Nome inválido. Tente novamente")
					nome_produto = input("Informe o nome do produto: ")

				nome_duplicado = True

				while nome_duplicado: 
					nome_duplicado = False
					for produto in produtos:
						if produto[0] == nome_produto:
							print("Já existe um produto com esse nome. Tente novamente.")
							nome_produto = input("Informe o nome do produto: ")
							nome_duplicado = True
							break

				kg = float(input("Informe o peso do produto: "))

				while kg <= 0:
					print("Peso inválido. Tente novamente")
					kg = float(input("Informe o peso do produto: "))

				preco = float(input("Informe o preço do produto: "))

				produtos.append([nome_produto, kg, 0, preco])
				print(f"O Produto {nome_produto} foi criado com sucesso.")

				novo_produto = input("Deseja criar um novo produto? (s/n): ").lower()

				if novo_produto != "s":
					break
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
		elif op == 9:
			print("=" * 40)
			print("         ESTOQUE ATUAL          ")
			print("=" * 40)

			print("")

			if len(produtos) == 0:
					print("Não possui nenhum produto cadastrado.")
			else:
				print("=" * 40)
				print(f"{"PRODUTO":<15} {"KG":<10} {"QUANTIDADE":<13}")
				print("=" * 40)
	
				for produto in produtos:
					print(f"{produto[0]:<15} {produto[1]:<10} {produto[2]:<13}")
				print("=" * 40)
				print(f"Total de Produtos: {len(produtos)}")
		elif op == 10:
			print("=" * 40)
			print("   PRODUÇÃO MENSAL DE LEITE   ")
			print("=" * 40)
			print("")

			maior_mes = 0

			for metrica in metricas:
				if metrica[1] > maior_mes:
					maior_mes = metrica[1]

			for metrica in metricas:
				valor = int(metrica[1] / 5)
				print(f"{metrica[0]} │ {'▇' * valor:<{int(maior_mes / 5) + 1}} {metrica[1]}L")	
		elif op == 11:
			print("=" * 40)
			print("   CADASTRAR USUÁRIO   ")
			print("=" * 40)

			print("")

			usuario = input("Digite o nome de usuário: ")

			while len(usuario) < 4:
				print("Nome de usuário inválido. O usuário deve ter no mínimo 4 caracteres.")
				usuario = input("Digite o nome de usuário: ")
			
			senha = input("Digite a senha: ")

			while len(senha) < 4:
				print("Senha inválida. A senha deve ter no mínimo 4 caracteres.")
				senha = input("Digite a senha: ")
			
			admin = input("Esse usuário terá permissão de administrador? (s/n): ").lower()

			if admin == "s":
				admin = True
			else:
				admin = False

			usuarios.append([usuario, senha, admin])
			print(f"Usuário '{usuario}' cadastrado com sucesso!")
		elif op == 12:
			print("Até logo! Obrigado por usar o sistema Fazenda Sertão.")
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
		print("7 - Sair")

		print("")

		op = int(input("Escolha uma opção: "))

		if op == 1:
			print("=" * 40)
			print("         ESTOQUE DISPONÍVEL          ")
			print("=" * 40)

			print("")

			while True:
				print("Qual estoque deseja visualizar?")
				print("1 - Estoque de Animais")
				print("2 - Estoque de Produtos")

				print("")

				op = int(input("Escolha (1-2): "))

				if op in (1, 2):
					break

			if op == 1:
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
			else:
				if len(produtos) == 0:
					print("Não possui nenhum produto cadastrado.")
				else:
					print("=" * 40)
					print(f"{"PRODUTO":<15} {"KG":<10} {"QUANTIDADE":<13}")
					print("=" * 40)

					for produto in produtos:
						print(f"{produto[0]:<15} {produto[1]:<10} {produto[2]:<13}")
					print("=" * 40)
					print(f"Total de Produtos: {len(produtos)}")
		elif op == 2:
			while True:
				print("=" * 40)
				print("            COMPRAR PRODUTO             ")
				print("=" * 40)

				print("")

				while True:
					print("Escolha um produto:")

					for i in range(len(produtos)):
						produto = produtos[i]
						print(f"{i + 1} - {produto[0]}")
					
					print("")

					op = int(input("Escolha: "))
					quantidade = int(input("Informe a quantidade que deseja comprar: "))
					
					confirmar_escolha = "s"

					while quantidade > produtos[op - 1][2]:
						print("Não há estoque suficiente desse produto. Tente novamente.")

						while True:
							confirmar_escolha = input("Deseja realizar novamente a compra? (s/n): ").lower()

							if confirmar_escolha in ("s", "n"):
								break

						if confirmar_escolha == "n":
							break

						quantidade = int(input(f"Informe a quantidade que deseja comprar do produto {produtos[op - 1][0]: }"))

					if confirmar_escolha == "n":
						break

					produtos[op - 1][2] -= quantidade
					print("Produto comprado com sucesso.")
					lista_compras.append([produtos[op - 1][0]])
					break

				nova_compra = input("Deseja realizar outra compra? (s/n): ").lower()

				if nova_compra != "s":
					break
		elif op == 3:
			print("=" * 40)
			print("            COMPRAR ANIMAL             ")
			print("=" * 40)

			print("")

			while True:
				print("Escolha um animal: ")

				disponivel_venda = False

				for i in range(len(animais)):
					animal = animais[i]

					if animal[2] == "Disponível p/ venda":
						disponivel_venda = True
						print(f"{i + 1} - {animal[0]} ({animal[1]})")

				if not disponivel_venda:
					print("Não possui animais a venda.")
					break

				op = int(input("Escolha uma opção: "))
				animal_selecionado = animais[op - 1]

				if animal_selecionado[2] != "Disponível p/ venda":
					print("Animal escolhido não está a venda. Tente novamente.")
					continue
				
				print(f"Animal de identificação ({animal_selecionado[1]}) foi adquirido com sucesso.")
				animais.pop(op - 1)
				lista_compras.append([animal_selecionado[1]])

				nova_compra = input("Deseja realizar outra compra? (s/n): ").lower()
				if nova_compra != "s":
					break
		elif op == 4:
			print("=" * 40)
			print("            AGENDAR RETIRADA             ")
			print("=" * 40)

			print("")

			while True:
				print("O que deseja agendar a retirada? ")

				if len(lista_compras) == 0:
					print("Você não possui nenhuma compra para agendar uma retirada.")
					break

				for i in range(len(lista_compras)):
					compra = lista_compras[i]

					print(f"{i + 1} - {compra[0]}")

				print("")

				op = int(input("Escolha: "))

				compra_selecionada = lista_compras[op - 1]

				data = input("Informe uma data para retirada (dd/mm/aaaa): ")
				hora = input("Informe o horário para retirada (hh:mm): ")

				while data == "":
					print("Data inválida. Tente novamente.")
					data = input("Informe uma data para retirada (dd/mm/aaaa): ")

				while hora == "":
					print("Horário inválido. Tente novamente.")
					hora = input("Informe o horário para retirada (hh:mm): ")

				print("Agendamento de retirada confirmado com sucesso.")
				agendamentos.append([data, hora, compra_selecionada[0]])
				lista_compras.pop(op - 1)

				novo_agendamento = input("Deseja realizar outro agendamento? (s/n): ")

				if novo_agendamento != "s":
					break
		elif op == 5:
			print("=" * 40)
			print("            REGISTRAR INTERESSES             ")
			print("=" * 40)

			print("")

			while True:
				print("Escolha um produto:")

				print("")

				for i in range(len(produtos)):
					produto = produtos[i]

					print(f"{i + 1} - {produto[0]}")

				print("")

				op = int(input("Escolha: "))

				duplicado = False

				for interesse in lista_interesses:
					if produtos[op - 1][0] == interesse[0]:
						duplicado = True
						break
					
				if duplicado:
					print("Você já adicionou esse produto aos seus interesses.")
				else:
					produto_selecionado = produtos[op - 1][0]

					lista_interesses.append([produto_selecionado])
					print("Produto adicionado aos seus interesses com sucesso.")

				novo_interesse = input("Deseja adicionar outro produto aos seus interesses? (s/n): ")

				if novo_interesse != "s":
					break
		elif op == 6:
			if len(lista_interesses) == 0:
					print("Você ainda não demonstrou interesse em nenhum produto.")
			else:
				print("=" * 40)
				print(f"{"MEUS INTERESSES":<40}")
				print("=" * 40)

				for interesse in lista_interesses:
					print(f"{interesse[0]:<40}")

				print("=" * 40)
		elif op == 7:
			print("Até logo! Obrigado por usar o sistema Fazenda Sertão.")
			break

			