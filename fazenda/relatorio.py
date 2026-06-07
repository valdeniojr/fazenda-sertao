from collections import Counter
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box

from database.dados import animais, metricas, produtos, historico
from utils.utils import titulo, clearCMD

console = Console()

def card(label, conteudo):
	console.print(
        Panel(
            conteudo,
            title=f"[bold white] {label} [/]",
            border_style="dim",
            box=box.ROUNDED,
            width=42,
            padding=(0, 1),
        )
    )

def animais_por_tipo():
	contagem = Counter(a["tipo"] for a in animais)

	tabela = Table(box=box.SIMPLE, show_header=True, header_style="dim", width=42, show_edge=False)
	tabela.add_column("Tipo", style="white")
	tabela.add_column("Quantidade", style="bold white", justify="left")

	for tipo, qtd in contagem.items():
		tabela.add_row(tipo, str(qtd))

	card("REBANHO POR TIPO", tabela)

	console.print(f" [dim]Total:[/] [bold white]{len(animais)}[/] "f"[dim]{'cabeças' if len(animais) != 1 else 'cabeça'}[/]")

def producao_leite():
	total = sum(m["producao"] for m in metricas)
	maior = max(m["producao"] for m in metricas)

	mes_destaque = next((m["mes"] for m in metricas if m["producao"] == maior and maior > 0), None)

	texto = Text()
	texto.append(f" {total:.1f} L\n", style="bold white")
	texto.append(" Total acumulado no ano\n", style="dim")

	if mes_destaque:
		texto.append("\n")
		texto.append(" ↑ Pico  ", style="bold green")
		texto.append(f" {mes_destaque}", style="white")
		texto.append(f" {maior:.1f} L", style="dim")

	card("PRODUÇÃO DE LEITE", texto)

def estoque_queijo():
	queijos = [p for p in produtos if "queijo" in p["nome"].lower()]
	total = sum(p["estoque"] for p in queijos)
	total_kg = sum(p["estoque"] * p["peso"] for p in queijos)

	tabela = Table(box=box.SIMPLE, show_header=True, header_style="dim", width=42, show_edge=False)
	tabela.add_column("Produto", style="white")
	tabela.add_column("Estoque", style="bold white")
	tabela.add_column("Peso total", style="dim")

	for p in queijos:
		tabela.add_row(p["nome"], f"x{p["estoque"]}", f"{p["estoque"] * p["peso"]:.1f} kg")

	card("ESTOQUE DE QUEIJO", tabela)
	console.print(f" [dim]Total:[/] [bold white]{total}[/] [dim white]un - {total_kg:.1f} kg[/]")

def relatorio_geral():
	clearCMD()
	titulo("RELATÓRIO GERAL DA FAZENDA")
	print("")

	animais_por_tipo()
	print("")
	producao_leite()
	print("")
	estoque_queijo()
	print("")

def registrar_movimentacao(acao, item, quantidade):
	data_atual = datetime.now().strftime("%d/%m/%Y")
	historico.append({"data": data_atual, "acao": acao, "item": item, "quantidade": quantidade})

def historico_movimentacoes():
	clearCMD()
	titulo("HISTÓRICO DE MOVIMENTAÇÃO")
	print("")

	if not historico:
		print("Nenhuma movimentação registrada ainda.")
		return
	
	tabela = Table(
		box=box.ROUNDED,
		border_style="dim",
		header_style="bold dim",
		show_header=True,
		show_lines=True,
		width=68,
	)
	
	tabela.add_column("Data", style="dim", width=17, no_wrap=True)
	tabela.add_column("Ação", width=20, no_wrap=True)
	tabela.add_column("Item", style="bold white", width=18)
	tabela.add_column("Qtd", style="white", width=6, justify="right")

	for mov in historico:
		tabela.add_row(mov["data"], mov["acao"], mov["item"], f"x{mov["quantidade"]}")

	console.print(tabela)
	console.print(f" [dim]Total de registros:[/] [bold white]{len(historico)}[/]\n")