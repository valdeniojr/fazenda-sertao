from dados import animais
from constantes import prefixos, tipos, animal_status

from utils import menu_opcoes, gerar_id, titulo, exibir_animal


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
				exibir_animal(animal)
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