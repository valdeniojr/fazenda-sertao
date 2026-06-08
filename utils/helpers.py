import os
import requests
from fpdf import FPDF
from datetime import datetime

def clearCMD():
  os.system('cls' if os.name == 'nt' else 'clear')

def buscar_endereco_por_cep(cep_destino):
    response = requests.get(
        f"https://viacep.com.br/ws/{cep_destino}/json/"
    )

    if response.status_code == 200:
        return response.json()

    return None

def gerar_id(lista_tipos, lista, tipo):

    if not tipo in lista_tipos:
        print("Não existe esse tipo de animal.")
        return
    
    prefixo = lista_tipos[tipo]
    i = 1

    while True:
        confirm = f"{prefixo}-{i:04d}"
        duplicado = False

        for animal in lista:
            if animal["identificacao"] == confirm:
                duplicado = True
                break

        if not duplicado:
            return confirm

        i += 1
    
def gerar_nota_fiscal(cliente, endereco, nome, quantidade, valor_total):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Times", "B", 24)
    pdf.cell(0, 15, "FAZENDA SERTÃO", ln=True, align="C")

    pdf.set_font("Times", "", 12)
    pdf.cell(0, 8, "Nota Fiscal", ln=True, align="C")

    pdf.ln(5)

    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    pdf.set_font("Times", "", 12)
    pdf.cell(32, 8, "Data de Emissão:")
    pdf.set_font("Times", "B", 12)
    pdf.cell(0, 8, datetime.now().strftime("%d/%m/%Y"), ln=True)

    pdf.ln(5)

    pdf.set_font("Times", "B", 14)
    pdf.cell(0, 10, "DADOS DO CLIENTE", ln=True)

    pdf.set_font("Times", "", 12)
    pdf.cell(0, 8, f"Cliente: {cliente}", ln=True)
    pdf.cell(0, 8, f"CEP: {endereco.get('cep')}", ln=True)
    pdf.cell(0, 8, f"Endereco: {endereco.get('logradouro')}", ln=True)
    pdf.cell(0, 8, f"Bairro: {endereco.get('bairro')}", ln=True)
    pdf.cell(0, 8, f"Cidade: {endereco.get('localidade')} - {endereco.get('uf')}", ln=True)

    pdf.ln(10)

    pdf.set_font("Times", "B", 12)

    pdf.cell(100, 10, "Produto", border=1)
    pdf.cell(40, 10, "Quantidade", border=1)
    pdf.cell(50, 10, "Valor", border=1, ln=True)

    pdf.set_font("Times", "", 12)

    pdf.cell(100, 10, f"{nome}", border=1)
    pdf.cell(40, 10, f"x{quantidade}", border=1)
    pdf.cell(50, 10, f"R$ {valor_total:.2f}", border=1, ln=True)

    pdf.ln(10)

    pdf.set_font("Times", "B", 14)
    pdf.cell(0, 10, f"VALOR TOTAL: R$ {valor_total:.2f}", ln=True)

    pdf.ln(20)

    pdf.cell(0, 10, "_" * 35, ln=True, align="C")
    pdf.cell(0, 8, "Assinatura do Responsável", align="C")

    pdf.output("notas/nota_fiscal.pdf")