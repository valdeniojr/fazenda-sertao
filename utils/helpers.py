import os

def clearCMD():
  os.system('cls' if os.name == 'nt' else 'clear')

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