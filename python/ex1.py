matriz = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
cont = 1
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o {cont}º valor: '))
        cont += 1
for l in range(0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('')