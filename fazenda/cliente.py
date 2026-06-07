from database.dados import animais, produtos
from utils.utils import menu_opcoes, titulo, exibir_produtos, exibir_animais, clearCMD
from fazenda.relatorio import registrar_movimentacao

def ver_estoque():
	clearCMD()
	titulo("ESTOQUE DISPONÍVEL")

	menu = ["Estoque de Animais", "Estoque de Produtos"]
	tipo_estoque = menu_opcoes("Qual estoque deseja visualizar?", menu, True)

	if tipo_estoque == 1:
		if len(animais) == 0:
			clearCMD()
			print("Nenhum animal cadastrado.")
		else:
			clearCMD()
			titulo("ESTOQUE DE ANIMAIS")
			exibir_animais(animais)
			print(f"Total de Animais: {len(animais)}")
	else:
		if len(produtos) == 0:
			clearCMD()
			print("Nenhum produto cadastrado.")
		else:
			clearCMD()
			titulo("ESTOQUE DE PRODUTOS")
			exibir_produtos(produtos)
			print(f"Total de Produtos: {len(produtos)}")