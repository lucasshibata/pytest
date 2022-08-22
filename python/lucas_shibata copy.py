'''Desenvolva o programa que leia vários números, armazene-os numa lista e mostre
estas informações:

a- Quantidade de elementos armazenados na lista;
b- Soma dos valores da lista;
c- Maior valor da lista;
d- Menor valor da lista;
e- Leia um valor e verificar se ele está na lista;
f- No item anterior, mostre também a posição (índice) do valor encontrado na pesquisa;
g- Mostre a lista na ordem crescente. Teste;
h- Insira (acrescente) o valor 33 na posição (índice) 1 da lista. Teste;
i- Mostre a lista na ordem decrescente. Teste;
j- Média dos valores da lista;
k- Porcentagem dos números maiores que dez na lista.
l- Crie o enunciado e a resposta de mais um item de exercício.'''
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
lista_nums = []
soma_tot = soma_maior = 0

# l - crie uma interface gráfica para facilitar a interatividade do usuário
def interface():
    print('================================')
    print('| bem vindo ao banco de dados  |')
    print('| 1- adicionar valores         |')
    print('| 2- quantidade de elementos   |')
    print('| 3- Soma dos valores da lista |')
    print('| 4- Maior valor da lista      |')
    print('| 5- Menor valor da lista      |')
    print('| 6- verificar se está na lista|')
    print('| 7- lista na ordem crescente  |')
    print('| 8- 33 na posição (índice) 1  |')
    print('| 9- lista decrescente         |')
    print('| 10- Média dos valores        |')
    print('| 11- Porcentagem > 10         |')
    print('| -1- exit                     |')
    print('================================')
    escolha = input('escolha uma opção:')
    return escolha

while True:
    escolha = interface()
    if int(escolha) == 1:
        print('Digite vazio para parar a repetição')
        while True:
            try:
                num = input('Insira um número para a lista: ')
                if num == '':
                    break
                else:
                    num = int(num)
                    lista_nums.append(num)
            except ValueError as e:
                print(f'\033[1;31m{e}\033[m, digite um número!')
                break
    elif int(escolha) == 2:
        print(f'existem {len(lista_nums)} números armazenados aqui')
    elif int(escolha) == 3:
        print(f'a soma dos números dessa lista é {sum(lista_nums)}')
    elif int(escolha) == 4:
        print(f'o maior número da lista é {max(lista_nums)}')
    elif int(escolha) == 5:
        print(f'o menor número da lista é {min(lista_nums)}')
    elif int(escolha) == 6:
        pesquisa = str(input('Deseja procurar um número na lista?[S/N]: ')).strip().upper()[0]
        while pesquisa in 'S':
            search = int(input('Insira o número que você deseja procurar: '))
            if search in lista_nums:
                print(f'Esse número está na lista!')
                resultado = lista_nums.index(search)
                print(f'A posição desse número na lista é {resultado}')
            else:
                print(f'Esse número não está na lista!')
        stop = str(input('Deseja parar?[S/N]: ')).strip().upper()[0]
        if stop in 'S':
            break
    elif int(escolha) == 7:
        lista_nums.sort()
        print(f'lista em ordem decrescente: {lista_nums}')
    elif int(escolha) == 8:
        lista_nums[1] = 33
        print(f'O número 33 foi adicionado na posição 1')
    elif int(escolha) == 9:
        lista_nums.sort(reverse=True)
        print(f'lista em ordem decrescente: {lista_nums}')
    elif int(escolha) == 10:
        media = sum(lista_nums) / len(lista_nums)
        print(f'média: {media}')
    elif int(escolha) == 11:
        for c in lista_nums:
            if c > 10:
                soma_maior += c
        pct_maior = soma_maior/len(lista_nums)*100
        print(f'Porcentagem dos números maiores que dez: {pct_maior}')
    else:
        break

