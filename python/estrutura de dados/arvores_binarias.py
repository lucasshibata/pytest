from random import randint

class NoDeArvoreBinaria():
    def __init__(self, numero= 0, filhoEsquerda= None, filhoDireita= None):
        self.numero = numero
        self.filhoEsquerda = filhoEsquerda
        self.filhoDireita = filhoDireita

    def Inserir(self, raiz, numero):
        if raiz == None:
            raiz = NoDeArvoreBinaria()
            raiz.numero = numero
        else:
            esquerda = bool(randint(0,1))
            if esquerda == True:
                raiz.filhoEsqueda = raiz.inserir(raiz.filhoEsquerda, numero)
            else:
                raiz.filhoDireita = raiz.inserir(raiz.filhoDireita, numero)
        return raiz

    def navegar(self, raiz, tipo):
        if tipo == 0:
            print(f'{raiz.numero}',end='')
            self.navegar(raiz.filhoEsquerda, tipo)
            self.navegar(raiz.filhoDireita, tipo)
        elif tipo == 1:
            self.navegar(raiz.filhoEsquerda, tipo)
            print(f'{raiz.numero}')
            self.navegar(raiz.filhoDireita, tipo)
        else:
            self.navegar(raiz.filhoEsquerda, tipo)
            self.navegar(raiz.filhoDireita, tipo)
            print(f'{raiz.numero}')


if __name__ == "__main__":
    raiz = NoDeArvoreBinaria(1)
    raiz = raiz.Inserir(raiz, raiz, 2)
    raiz = raiz.Inserir(raiz, raiz, 3)
    raiz = raiz.Inserir(raiz, raiz, 4)
    raiz = raiz.Inserir(raiz, raiz, 5)
    raiz = raiz.Inserir(raiz, raiz, 6)
    raiz = raiz.Inserir(raiz, raiz, 7)
    raiz = raiz.Inserir(raiz, raiz, 8)

    raiz.navegação(0)
    raiz.navegação(1)
    raiz.navegação(2)

