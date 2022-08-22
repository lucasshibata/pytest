def menu():
    print('[C] - create\n'
    '[R] - read\n'
    '[U] - updade\n'
    '[D] - delete\n'
    '[S] - sair')
    opcao = str(input('insira uma opção: ')).strip().upper()[0]
    if opcao not in 'CRUDS':
        print('Opção inválida')
    return opcao

def create():
    palavra = str(input('Digite uma palavra para a lista: '))
    lista.append(palavra)

def read():
    if lista != []:
        print('\n','-='*10)
        for c in lista:
            print(c)
        print('-='*10,'\n')
    else:
        print('\n','-='*10)
        print('lista vazia')
        print('-='*10,'\n')

def update():
    read()
    cor_init = '\033[1;31m'
    cor_fim = '\033[m'
    try: 
        numero = int(input('Digite a posição que deseja mudar: '))
        nova_palavra = str(input('Digite a palavra que substituirá: '))
        lista[numero] = nova_palavra
    except IndexError as e:
        print(f'{cor_init}<<{e}>>{cor_fim} Posição inválida! Tente novamente.')
    except ValueError as e:
        print(f'{cor_init}<<{e}>>{cor_fim} Valor primitivo inválido, por favor digite um número!')

def delete():
    read()
    if lista != []:
        palavra = str(input('Digite a palavra a ser deletada: '))
        if palavra in lista:
            lista.remove(palavra)
        else:
            print('Essa palavra não exista na lista')
    else:
        print('Não tem palavras para serem apagadas')


if __name__ == "__main__":
    lista = []
    while True:
        op = menu()
        if op in 'C':
            create()
        elif op in 'R':
            read()
        elif op in 'U':
            update()
        elif op in 'D':
            delete()
        elif op in 'S':
            break

