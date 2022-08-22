#políticas FILO (first in - last out)
class No:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None
    
    def push(self, cabeca, elemento):
        elemento.proximo = cabeca
        cabeca = elemento
        return cabeca

    def pop(self, cabeca):
        print(f'Desempilhar: {cabeca.numero}')
        cabeca = cabeca.proximo
        return cabeca

    def top(self, cabeca):
        print(f'ver: {cabeca.numero}')



if __name__ == "__main__":
    cabeca = No(None)
    opcao = 0
    
    while opcao != 4:
        print('===================\n'
        '| Menu de Opções |\n'
        '=====================\n'
        '| 1 - empilhar |\n'
        '| 2 - desempilhar |\n'
        '| 3 - ver |\n'
        '| 4 - sair |\n'
        '======================')
        opcao = int(input('Insira sua opção: '))
        if opcao == 1:
            num = int(input('Digite o número: '))
            cabeca = cabeca.push(cabeca, No(num))
        elif opcao == 2:
            cabeca = cabeca.pop(cabeca)
        elif opcao == 3:
            cabeca.top(cabeca)