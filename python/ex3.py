'''def valor_absoluto(num):
    if num < 0:
        num = num*(-1)
        print(f'valor absoluto desse número é {num}')
    else:
        print(f'valor absoluto desse número é {num}')


if __name__ == "__main__":
    numero = float(input('Insira um valor: '))
    valor_absoluto(numero)
    print(f'{abs(-3)}')'''

#-=-=-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-=-=--=-=-==-

'''def menu():
    opcao = str(input('insira uma opção [+]/[-]/[*]: '))
    lista_str = ['+','-', '*']
    while opcao not in lista_str:
        print('Opção inválida!')
        opcao = str(input('insira uma opção [+]/[-]/[*]: '))
    return opcao

def soma(x, y):
    result = x + y
    return result

def subtrai(x, y):
    result = x - y
    return result

def multi(x, y):
    result = x * y
    return result


if __name__ == "__main__":
    v1 = int(input('primeiro valor: '))
    v2 = int(input('segundo valor: '))
    opc = menu()
    if opc in '+':
        result = soma(v1, v2)
        print(f'{result}')
    elif opc in '-':
        result = subtrai(v1, v2)
        print(f'{result}')
    elif opc in '*':
        result = multi(v1, v2)
        print(f'{result}')'''

#-=-=-=-=-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=-=-=--=-=-==-        