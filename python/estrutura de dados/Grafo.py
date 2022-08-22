def construir(grafo):
	for i in range(0, 5):
		print("========================================")
		print("Indicação da vizinhança do vértice " + str(i))
		print("========================================")
		for j in range(0, 5):
			if i != j:
				conexao = input("Digite <S> para indicar que o vértice " + str(j) + " é vizinho: ")
				if conexao in "s":
					grafo[i][j] = 1

def imprimirConexoes(grafo):
	for i in range(0, 5):
		for j in range(0, 5):
			print(grafo[i][j], end ="\t")
		print("")
	for i in range(0, 5):
		for j in range(0, 5):
			if (grafo[i][j] == 1):
				print("(" + str(i) + ", " + str(j) + ")")

def descobrirVerticeMaisPopular(grafo):
	verticeMaisPopular = 0
	maiorQtdDeVizinhos = 0

	for i in range(0, 5):
		qtdVizinhos = 0
		for j in range(0, 5):
			if (grafo[i][j] == 1):
				qtdVizinhos +=1

		if (qtdVizinhos > maiorQtdDeVizinhos):
			verticeMaisPopular = i
			maiorQtdDeVizinhos = qtdVizinhos
		
	print("O vértice maior popular é o " + str(verticeMaisPopular))
	print("Ele tem " + str(maiorQtdDeVizinhos) + " vizinhos")

grafo = [[0] * 5] * 5

imprimirConexoes(grafo)

construir(grafo)

imprimirConexoes(grafo)

descobrirVerticeMaisPopular(grafo)
