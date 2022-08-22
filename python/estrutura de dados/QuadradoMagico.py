#declaração de valores
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_linha1 = sum_linha2 = sum_linha3 = sum_coluna1 = sum_coluna2 = sum_coluna3 = sum_diagonal1 = sum_diagonal2 = 0

#preenchimento da matriz
for l in range(0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o valor [{l}][{c}]: '))

#devolutiva da matriz
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')

#verificação de valores da matriz
#linhas
for i in range(0, 3):
    sum_linha1 += matriz[0][i]
    sum_linha2 += matriz[1][i]
    sum_linha3 += matriz[2][i]
if sum_linha1 != 15:
    print('valores da linha 1 não compatíveis')
if sum_linha2 != 15:
    print('valores da linha 2 não compatíveis')
if sum_linha3 != 15:
    print('valores da linha 3 não compatíveis')    

#colunas
for i in range(0, 3):
    sum_coluna1 += matriz[i][0]
    sum_coluna2 += matriz[i][1]
    sum_coluna3 += matriz[i][2]

if sum_coluna1 != 15:
    print('valores da coluna 1 não compatíveis')
if sum_coluna2 != 15:
    print('valores da coluna 2 não compatíveis')
if sum_coluna3 != 15:
    print('valores da coluna 3 não compatíveis')

#diagonais
for i in range(0, 3):
    sum_diagonal1 += matriz[i][i]
sum_diagonal2 = matriz[2][0] + matriz[1][1] + matriz[0][2]
if sum_diagonal1 != 15:
    print('valores da diagonal 1 não compatíveis')
if sum_diagonal2 != 15:
    print('valores da diagonal 2 não compatíveis')