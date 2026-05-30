from auth import login
from fazenda import cadastrar_animal

def menu(permissao):
	if permissao:
		print("=" * 40)
		print("          MENU DO ADMINISTRADOR          ")
		print("=" * 40)

		print("")

		print("1 - Cadastrar Animal")
		print("2 - Buscar Animal")
		print("3 - Atualizar Animal")
		print("4 - Remover Animal")
		print("5 - Listar Animais")
		print("6 - Registrar Produção de Leite")
		print("7 - Cadastrar Produto")
		print("8 - Adicionar Produto ao Estoque")
		print("9 - Ver Estoque Atual")
		print("10 - Gráfico de Produção de Leite")
		print("11 - Cadastrar Usuário")
		print("12 - Sair")

		print("")

		op = int(input("Escolha uma opção: "))

		if op == 1:
			cadastrar_animal()
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

def main():
	is_admin = login()
	menu(is_admin)

main()