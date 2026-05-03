usuarios = [
	["johndoe", "12345", True], # Usuário teste
	["janedoe", "12345", False] # Usuário teste
]

animais = [
	["Ovino", "2232", "Para engorda"]
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
		print("5 - Listar Animal")

		print("")

		print("6 - Registrar Produção de Leite")
		print("7 - Adicionar Produto ao Estoque")
		print("8 - Ver Estoque Atual")

		print("")

		print("9 - Extra")

		print("")

		op = int(input("Escolha uma opção: "))

		## Funcionalidades

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
						print(f"Indentificação: {animal[1]}")
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
			print(4)						
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