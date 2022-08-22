#algoritmos de ordenação
'''lista = []
while True:
    lista.append(int(input('Insira um valor: ')))
    stop = str(input('deseja parar?: ')).strip().upper()[0]
    if stop in 'S':
        break
for i in range(0, len(lista) - 1) :
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[i]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp

print(lista)'''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''lista = [5, 10, 7 , 6, 1, 9]
while True:
    lista.append(int(input('Insira um valor: ')))
    stop = str(input('deseja parar?: ')).strip().upper()[0]
    if stop in 'S':
        break
houve_troca = True
while (houve_troca == True):
    houve_troca = False
    i = 0
    while (i < len(lista)-1):
        if lista[i] > lista[i+1]:
            temp = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = temp
            houve_troca = True
        i +=1
print(lista)'''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#algoritmos de busca
'''from random import randint
repet = int(input('insira as repetições: '))
cont = 0
lista =[]
while cont != repet:
    lista.append(randint(0, 100))
    cont +=1
valor = int(input('digite o valor a ser procurado: '))
encontrei = False
for i in lista:
    if i == valor:
        encontrei = True

if encontrei == True:
    print('Achei')
else:
    print('não achei')'''

#algoritmos de busca binária
from random import randint
repet = int(input('insira as repetições: '))
cont = 0
lista =[]
while cont != repet:
    lista.append(randint(0, 10))
    cont +=1

valor = int(input('digite o valor a ser procurado: '))
encontrei = -1

#ordenação
for i in range(0, len(lista) - 1) :
    for j in range(i + 1, len(lista)):
        if lista[j] < lista[i]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp

#processamento
inicio = 0
fim = len(lista)
while True:
    meio = int((inicio + fim)/2)
    if lista[meio] == valor:
        encontrei = meio
        break
    else:
        if lista[meio] > valor:
            fim = meio
        else:
            inicio = meio
        if inicio == fim:
            break

if encontrei > -1:
    print('Achei')
    print(lista)
else:
    print('não achei')
    print(lista)