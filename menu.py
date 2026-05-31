from fazenda import cadastrar_animal

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

texto_menu = Text()

texto_menu.append("\n  Animais\n \n", style="dim")
texto_menu.append("  1 - ", style="dim")
texto_menu.append("Cadastrar Animal\n", style="white")
texto_menu.append("  2 - ", style="dim")
texto_menu.append("Buscar Animal\n", style="white")
texto_menu.append("  3 - ", style="dim")
texto_menu.append("Atualizar Animal\n", style="white")
texto_menu.append("  4 - ", style="dim")
texto_menu.append("Remover Animal\n", style="white")
texto_menu.append("  5 - ", style="dim")
texto_menu.append("Listar Animais\n\n", style="white")

texto_menu.append("  Produção\n \n", style="dim")
texto_menu.append("  6 - ", style="dim")
texto_menu.append("Registrar Produção de Leite\n", style="white")
texto_menu.append("  7 - ", style="dim")
texto_menu.append("Gráfico de Produção de Leite\n\n", style="white")

texto_menu.append("  Estoque\n \n", style="dim")
texto_menu.append("  8 - ", style="dim")
texto_menu.append("Cadastrar Produto\n", style="white")
texto_menu.append("  9 - ", style="dim")
texto_menu.append("Adicionar Produto ao Estoque\n", style="white")
texto_menu.append("  10 - ", style="dim")
texto_menu.append("Ver Estoque Atual\n\n", style="white")

texto_menu.append("  Sistema\n \n", style="dim")
texto_menu.append("  11 - ", style="dim")
texto_menu.append("Cadastrar Usuário\n", style="white")

texto_menu.append("  12 - ", style="dim")
texto_menu.append("Sair\n\n", style="white")


def menu(permissao):
	if permissao:
		console.print(
		    Panel(
		        texto_menu,
		        title="[bold white] FAZENDA SERTÃO [/]",
		        subtitle="[dim]Menu do Administrador[/]",
		        border_style="dim",
		        box=box.ROUNDED,
		        width=42,
		        padding=(0, 1),
		    )
		)

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