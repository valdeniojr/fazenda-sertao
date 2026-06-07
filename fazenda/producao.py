from database.dados import metricas
from utils.utils import menu_opcoes, titulo, clearCMD

def producao_leite():
	clearCMD()
	titulo("PRODUÇÃO DE LEITE")

	litros = float(input("Informe a produção diária em litros: "))

	while litros < 0:
		clearCMD()
		print("Valor inválido. Tente novamente")
		litros = float(input("Informe a produção diária em litros: "))

	meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
	         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	clearCMD()
	mes = menu_opcoes("Produção Diária", meses, True)

	metricas[mes - 1]["producao"] += litros
	clearCMD()
	print(f"Produção de {litros}L registrada com sucesso!")

def grafico_producao():
	clearCMD()
	titulo("PRODUÇÃO MENSAL DE LEITE")

	maior_mes = 0

	for metrica in metricas:
		if metrica["producao"] > maior_mes:
			maior_mes = metrica["producao"]

	for metrica in metricas:
		valor = int(metrica["producao"] / 5)
		print(f"{metrica['mes']} ┤ {'█' * valor:<{int(maior_mes / 5) + 1}} {metrica['producao']}L")
