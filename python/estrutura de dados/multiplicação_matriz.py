# 1) para multiplicar 2 matrizes, o nº de colunas da 1ª deve ser igual
# ao nº de linhas da 2ª
# 2) o resultado será uma matriz com nº de linhas igual ao da 1ª e
# o nº de colunas igual ao da 2ª.
from random import randint

matriz1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# matrizes aleatórias
for l in range(0, 3):
    for c in range (0, 3):
        matriz1[l][c] = randint(0, 50)
for l in range(0, 3):
    for c in range (0, 3):
        matriz2[l][c] = randint(0, 50)

for l in range(0, 3):
    for c in range (0, 3):
        matriz1[l][c] = matriz1[l][c]

for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz1[l][c]:^5}]', end='')
    print('')