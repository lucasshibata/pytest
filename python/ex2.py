'''dado = int(input('Insira o número de lados do dado: '))
print('Esses são os valores possiveis: ')
for l in range (1, dado + 1):
    print(l)'''

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

'''list_dado = []
dado = int(input('Insira o número de lados do dado: '))
print('Esses são os valores possiveis: ')
for l in range (1, dado + 1):
    list_dado.append(l)
for c in list_dado:
    print(c)'''

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''cont = 0
for l1 in range(1, 7):
    for l2 in range(1, 7):
        if l1 + l2 == 7:
            print(f' {l1} -- {l2} /', end='')
            cont +=1
print('')
print(f'foram geradas {cont} repetições')'''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''for c in range(0, 2):
    for d in range(0, 2):
        for u in range(0, 2):
            valor = c * 2**2 + d * 2**1 + u * 2 **0            
            print(f'{valor} - ',end='') 
            print(f'{c}{d}{u}')'''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''for num in range(0, 8):
    print(f'{num} - ', end='')
    print(f'{bin(num)[2:]}')
    prin((f'{num:.2f}'))'''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''def soma_valores(v1, v2):
    result = v1 + v2
    return result

if __name__ == "__main__":
    soma = soma_valores(3, 2)
    print(soma)'''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def somar(v1, v2):
    result = v1 + v2
    return result


def subtrair(v1, v2):
    result = v1 - v2
    return result


if __name__ == '__main__':
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    result_soma = somar(num1, num2)
    result_sub = subtrair(num1, num2)
    print(f'resultado da soma: {result_soma}\n'
    f'resultado da subtração: {result_sub}')

