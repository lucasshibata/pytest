# exercício 1 -
'''maior = menor = homens = mulheres = cont = 0
while True:
    sexo = str(input('Insira seu sexo[M/F]: ')).upper().strip()[0]
    altura = float(input('Insira a sua altura: '))
    cont += 1
    if cont == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura
    if sexo in 'M':
        homens += 1
    if sexo in 'F':
        mulheres += 1

    stop = str(input('Deseja parar?[S/N]: ')).upper().strip()[0]
    if stop in 'S':
        break
print('')
print('-='*15)
print(f'número de homens: {homens}\n'
f'numero de mulheres: {mulheres}\n'
f'maior altura do grupo: {maior}\n'
f'menor altura do grupo: {menor}')
print('-='*15)
print('')'''

#exercício 2 - 
l_altura = []
l_genero = []
while True:
    sexo = str(input('Insira o sexo[M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Insira o sexo[M/F]: ')).upper().strip()[0]
    altura = float(input('Insira a altura: '))
    l_genero.append(sexo)
    l_altura.append(altura)

    stop = str(input('Deseja parar?[S/N]: ')).upper().strip()[0]
    if stop in 'S':
        break

print('')
print('-='*15)
print(f'número de homens: {l_genero.count("M")}\n'
f'numero de mulheres: {l_genero.count("F")}\n'
f'maior altura do grupo: {max(l_altura)}\n'
f'menor altura do grupo: {min(l_altura)}\n'
f'media de altura do grupo: {sum(l_altura)/len(l_genero):.2f}')
print('-='*15)
print('')
