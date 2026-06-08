import os
import requests

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