from dados import animais
from constantes import prefixos, tipos, animal_status

from utils import menu_opcoes, gerar_id


def cadastrar_animal ():
	print("=" * 40)
	print("          CADASTRAR ANIMAL          ")
	print("=" * 40)
	print("")
	
	tipo_escolhido = menu_opcoes("Tipo de Animal", tipos)
	identificacao = gerar_id(prefixos, animais, tipo_escolhido)
	status_escolhido = menu_opcoes("Status do Animal: ", animal_status)
	
	animais.append({"tipo": tipo_escolhido, "identificacao": identificacao, "status": status_escolhido})
	print(f"Animal '{identificacao}' cadastrado com sucesso!")