from dados import animais
from constantes import prefixos, tipos, animal_status

from utils import menu_opcoes, gerar_id, titulo


def cadastrar_animal ():
	titulo("CADASTRAR ANIMAL")
	
	tipo_escolhido = menu_opcoes("Tipo de Animal", tipos)
	identificacao = gerar_id(prefixos, animais, tipo_escolhido)
	status_escolhido = menu_opcoes("Status do Animal: ", animal_status)
	
	animais.append({"tipo": tipo_escolhido, "identificacao": identificacao, "status": status_escolhido})
	print(f"Animal '{identificacao}' cadastrado com sucesso!")

def buscar_animal ():
	titulo("BUSCAR ANIMAL")

	while True:
		identificacao = input("Informe a identificação do animal (brinco ou nº único) [ex: BOV-0001]: ")

		for animal in animais:
			if animal[1] == identificacao:
				print("========== RESULTADO DA BUSCA ==========")
				print(f"Tipo: {animal[0]}")
				print(f"Identificação: {animal[1]}")
				print(f"Status: {animal[2]}")
				print("=" * 40)
				break
		else:
			print("Nenhum animal com essa identificação foi encontrado.")

		nova_busca = input("Deseja realizar uma nova busca? (s/n): ").lower()

		if nova_busca != "s":
			break