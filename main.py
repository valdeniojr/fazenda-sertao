usuarios = [
	["johndoe", "12345", True], # Usuário teste
	["janedoe", "12345", False] # Usuário teste
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