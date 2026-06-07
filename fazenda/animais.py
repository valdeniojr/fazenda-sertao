from database.dados import animais
from config.constantes import prefixos, tipos, animal_status
from utils.utils import menu_opcoes, gerar_id, titulo, exibir_animais
from utils.helpers import clearCMD

def cadastrar_animal():
	clearCMD()
	titulo("CADASTRAR ANIMAL")

	tipo_escolhido = menu_opcoes("Tipo de Animal", tipos, False)
	identificacao = gerar_id(prefixos, animais, tipo_escolhido)
	status_escolhido = menu_opcoes("Status do Animal", animal_status, False)

	clearCMD()
	animais.append({"tipo": tipo_escolhido, "identificacao": identificacao, "status": status_escolhido})
	print(f"Animal '{identificacao}' cadastrado com sucesso!")


def buscar_animal():
	clearCMD()
	titulo("BUSCAR ANIMAL")
	while True:
		identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

		for animal in animais:
			if animal["identificacao"] == identificacao:
				exibir_animais([animal])
				break
		else:
			clearCMD()
			print("Nenhum animal com essa identificação foi encontrado.")

		nova_busca = input("Deseja realizar uma nova busca? (s/n): ").lower()

		if nova_busca != "s":
			clearCMD()
			break


def atualizar_animal():
	clearCMD()
	titulo("ATUALIZAR ANIMAL")

	while True:
		menu = ["Tipo", "Identificação", "Status"]
		campo = menu_opcoes("Qual informação deseja atualizar?", menu, True)

		if campo == 1:
			clearCMD()
			identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

			for animal in animais:
				if animal["identificacao"] == identificacao:
					tipo_escolhido = menu_opcoes("Tipo de Animal", tipos, False)
					animal["tipo"] = tipo_escolhido
					clearCMD()
					print(f"Animal '{animal['identificacao']}' atualizado com sucesso!")
					break
			else:
				clearCMD()
				print("Nenhum animal com essa identificação foi encontrado.")

		elif campo == 2:
			clearCMD()
			identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

			for animal in animais:
				if animal["identificacao"] == identificacao:
					nova_identificacao = input("Informe a nova identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

					duplicado = True

					while duplicado:
						duplicado = False
						for a in animais:
							if a["identificacao"] == nova_identificacao:
								duplicado = True
								clearCMD()
								print(f"Identificação '{nova_identificacao}' já está em uso.")
								nova_identificacao = input("Informe a nova identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")
								break

					clearCMD()
					animal["identificacao"] = nova_identificacao
					print(f"Animal '{animal['identificacao']}' atualizado com sucesso!")
					break
			else:
				clearCMD()
				print("Nenhum animal com essa identificação foi encontrado.")

		elif campo == 3:
			clearCMD()
			identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

			for animal in animais:
				if animal["identificacao"] == identificacao:
					status_escolhido = menu_opcoes("Status do Animal: ", animal_status, False)
					animal["status"] = status_escolhido
					clearCMD()
					print(f"Animal '{animal['identificacao']}' atualizado com sucesso!")
					break
			else:
				clearCMD()
				print("Nenhum animal com essa identificação foi encontrado.")

		nova_alteracao = input("Deseja realizar uma nova alteração? (s/n): ").lower()

		if nova_alteracao != "s":
			clearCMD()
			break


def remover_animal():
	clearCMD()
	titulo("REMOVER ANIMAL")

	while True:
		identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

		for i in range(len(animais)):
			animal = animais[i]

			if animal["identificacao"] == identificacao:
				exibir_animais([animal])

				confirmar_remocao = input("Tem certeza que deseja remover este animal? (s/n): ").lower()

				if confirmar_remocao != "n":
					animais.pop(i)
					clearCMD()
					print("Animal removido com sucesso!")
				break
		else:
			clearCMD()
			print("Nenhum animal com essa identificação foi encontrado.")

		nova_remocao = input("Deseja realizar uma nova remoção? (s/n): ").lower()

		if nova_remocao != "s":
			clearCMD()
			break


def listar_animais():
	clearCMD()
	if len(animais) == 0:
		print("Nenhum animal cadastrado.")
	else:
		titulo("LISTA DE ANIMAIS")
		exibir_animais(animais)
		print(f"Total de Animais: {len(animais)}")
