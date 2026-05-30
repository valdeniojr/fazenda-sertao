def menu_opcoes(titulo, lista):
	while True:
		print(titulo)
		for i in range(len(lista)):
			print(f"{i + 1} - {lista[i]}")
		
		index = int(input(f"Escolha (1-{len(lista)}): "))

		if index > 0 and index <= len(lista):
			break
		else:
			print("Opção inválida. Tente novamente.")

	return lista[index - 1]

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

