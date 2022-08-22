'''def fatorial(num=3):
    result = 1
    if num < 0:
        print('Valor não permitido!')
    else:
        for c in range(1, num+1):
            result = result * c
        return result


if __name__ == "__main__":
    try:
        num = int(input('digite um número para ver seu fatorial: '))
        resultado = fatorial(num)
    except ValueError:
        resultado = fatorial()
        num = 3
    print(f'fatorial de {num} é: {resultado}')'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=--==--==
'''from math import factorial
f1 = factorial(5)
print(f1)'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=--==--==
'''def potencia ():
    base = int(input('base: '))
    expoente = int(input('expoente: '))
    print(f'potencia = {base ** expoente}')

if __name__ == "__main__":
    potencia()'''
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=--==--==
""" def convente_em_minuto(hora, minuto):
    result = hora * 60 + minuto
    return result

if __name__ == "__main__":
    hora = int(input('hora:'))
    minuto = int(input('minuto: '))
    resultado = convente_em_minuto(hora, minuto)
    print(f'o tempo total é de {resultado} minutos') """
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=--==--==
lista = []
while True:
    num = int(input('insira um valor: '))
    lista.append(num)
    stop = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
    if stop in 'N':
        break
# a
print(len(lista))
#b
print(sum(lista))
#c
print(max(lista))
#d
print(min(lista))

#g
print(lista.sort())
#i
print(lista.sort(reverse=True))
#j
print(sum(lista)/len(lista))
#k
soma = 0
for num in lista:
    if num > 10:
        soma += 1
print(soma/len(lista)*100)


