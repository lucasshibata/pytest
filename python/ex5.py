def menu():
    print('[C] - create\n'
    '[R] - read\n'
    '[U] - updade\n'
    '[D] - delete\n'
    '[S] - sair')
    opcao = str(input('insira uma opção: ')).strip().upper()[0]
    return opcao

def create():
    palavra = str(input('Digite uma palavra para a lista: '))
    lista.append(palavra)

def read():
    print(lista)

def update():
    try: 
        numero = int(input('Digite a posição que deseja mudar: '))
        nova_palavra = str(input('Digite a palavra que substituirá: '))
        lista[numero] = nova_palavra
    except IndexError:
        print('Posição inválida! Tente novamente.')
    except ValueError:
        print('Valor primitivo inválido, por favor digite um número!')

def delete():
    palavra = str(input('Digite a palavra a ser deletada: '))
    lista.remove(palavra)


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

