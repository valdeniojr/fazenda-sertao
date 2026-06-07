from database.dados import usuarios
from utils.utils import titulo
from utils.helpers import clearCMD

def cadastrar_usuario():
	clearCMD()
	titulo("CADASTRAR USUÁRIO")

	usuario = input("Digite o nome de usuário: ")

	duplicado = True
	
	while duplicado:
		duplicado = False
		for user in usuarios:
			if user["usuario"] == usuario:
				clearCMD()
				print("Já existe um usuário com esse nome. Tente novamente.")
				usuario = input("Digite o nome de usuário: ")
				duplicado = True
				break

	while len(usuario) < 4:
		clearCMD()
		print("Nome de usuário inválido. O usuário deve ter no mínimo 4 caracteres.")
		usuario = input("Digite o nome de usuário: ")
	
	senha = input("Digite a senha: ")

	while len(senha) < 4:
		clearCMD()
		print("Senha inválida. A senha deve ter no mínimo 4 caracteres.")
		senha = input("Digite a senha: ")
	
	permissao = input("Esse usuário terá permissão de administrador? (s/n): ").lower()

	if permissao == "s":
		permissao = True
	else:
		permissao = False

	usuarios.append({"usuario": usuario, "senha": senha, "permissao": permissao})
	clearCMD()
	print(f"Usuário '{usuario}' cadastrado com sucesso!")