class NoDeArvoreDeBusca:
    def __init__(self, valor=None, filho_esquerda=None, filho_direita=None):
        self.valor = valor
        self.filhoEsquerda = filho_esquerda
        self.filhoDireita = filho_direita

    def inserir_elemento(raiz, valor):
        if raiz == None:
            raiz = NoDeArvoreDeBusca()
            raiz.valor = valor
        elif valor < raiz.valor:
            raiz.filhoEsquerda = NoDeArvoreDeBusca.inserir_elemento(raiz.filhoEsquerda, valor)
        else:
            raiz.filhoDireita = NoDeArvoreDeBusca.inserir_elemento(raiz.filhoDireita, valor)
        return raiz


    def buscar_elemento(raiz, valor, caminho):
        if raiz == None:
            print(f'não achei o valor')
        elif valor == raiz.valor:
            print(f'\nAchei o valor no caminho {caminho}')
        elif valor < raiz.valor:
            NoDeArvoreDeBusca.buscar_elemento(raiz.filhoEsquerda, valor, caminho + 'esquerda, ')
        else:
            NoDeArvoreDeBusca.buscar_elemento(raiz.filhoDireita, valor, caminho + 'direita, ')


    def navergar_arvore(raiz):
        if raiz != None:
            NoDeArvoreDeBusca.navergar_arvore(raiz.filhoEsquerda)
            print(f'{raiz.valor}', end=' ')
            NoDeArvoreDeBusca.navergar_arvore(raiz.filhoDireita)


if __name__ == "__main__":
    raiz = None
    raiz = NoDeArvoreDeBusca.inserir_elemento(raiz, 12)
    
    while True:
        num = int(input('Digite o valor: '))
        raiz = NoDeArvoreDeBusca.inserir_elemento(raiz, num)
        stop = input('deseja parar?[S/N]: ').upper().strip()[0]
        if stop in 'S':
            break

    NoDeArvoreDeBusca.buscar_elemento(raiz, 1000, 'raiz ')
    NoDeArvoreDeBusca.buscar_elemento(raiz, 12, 'raiz ')
    NoDeArvoreDeBusca.buscar_elemento(raiz, 10, 'raiz ')
    NoDeArvoreDeBusca.buscar_elemento(raiz, 23, 'raiz ')

    NoDeArvoreDeBusca.navergar_arvore(raiz)
    
        
