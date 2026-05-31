from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

from utils import titulo
from fazenda import cadastrar_animal

console = Console()

menu_admin = Text()

menu_admin.append("\n  Animais\n \n", style="dim")
menu_admin.append("  1 - ", style="dim")
menu_admin.append("Cadastrar Animal\n", style="white")
menu_admin.append("  2 - ", style="dim")
menu_admin.append("Buscar Animal\n", style="white")
menu_admin.append("  3 - ", style="dim")
menu_admin.append("Atualizar Animal\n", style="white")
menu_admin.append("  4 - ", style="dim")
menu_admin.append("Remover Animal\n", style="white")
menu_admin.append("  5 - ", style="dim")
menu_admin.append("Listar Animais\n\n", style="white")

menu_admin.append("  Produção\n \n", style="dim")
menu_admin.append("  6 - ", style="dim")
menu_admin.append("Registrar Produção de Leite\n", style="white")
menu_admin.append("  7 - ", style="dim")
menu_admin.append("Gráfico de Produção de Leite\n\n", style="white")

menu_admin.append("  Estoque\n \n", style="dim")
menu_admin.append("  8 - ", style="dim")
menu_admin.append("Cadastrar Produto\n", style="white")
menu_admin.append("  9 - ", style="dim")
menu_admin.append("Adicionar Produto ao Estoque\n", style="white")
menu_admin.append("  10 - ", style="dim")
menu_admin.append("Ver Estoque Atual\n\n", style="white")

menu_admin.append("  Sistema\n \n", style="dim")
menu_admin.append("  11 - ", style="dim")
menu_admin.append("Cadastrar Usuário\n", style="white")

menu_admin.append("  12 - ", style="dim")
menu_admin.append("Sair\n", style="white")

menu_cliente = Text()

menu_cliente.append("\n  1 - ", style="dim")
menu_cliente.append("Ver Estoque Disponível\n", style="white")
menu_cliente.append("  2 - ", style="dim")
menu_cliente.append("Comprar Produto\n", style="white")
menu_cliente.append("  3 - ", style="dim")
menu_cliente.append("Comprar Animal\n", style="white")
menu_cliente.append("  4 - ", style="dim")
menu_cliente.append("Agendar Retirada\n", style="white")
menu_cliente.append("  5 - ", style="dim")
menu_cliente.append("Registrar Interesse em Produto\n", style="white")
menu_cliente.append("  6 - ", style="dim")
menu_cliente.append("Ver Meus Interesses\n", style="white")
menu_cliente.append("  7 - ", style="dim")
menu_cliente.append("Sair\n", style="white")


def menu(permissao):
	while True:
		if permissao:
			titulo("FAZENDA SERTÃO")
			console.print(
			    Panel(
			        menu_admin,
			        title="[bold white] MENU ADMINISTRADOR [/]",
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
			titulo("FAZENDA SERTÃO")
			console.print(
			    Panel(
			        menu_cliente,
			        title="[bold white] MENU CLIENTE [/]",
			        border_style="dim",
			        box=box.ROUNDED,
			        width=42,
			        padding=(0, 1),
			    )
			)

			print("")

			op = int(input("Escolha uma opção: "))