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