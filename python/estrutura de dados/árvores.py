# é obrigatório estabelecer quem é a raiz da árvore
# ordem = a quantidade de filhos dos nós
# nível = a distância entre um nó e a raiz
# altura = maior nível entre todas as folhas da árvore + 1

from random import randint

class No:
    def __init__(self, elemento=0):
        self.elemento = elemento
        self.filho1 = None
        self.filho2 = None
        self.filho3 = None
        self.filho4 = None
        self.filho5 = None

    def inserir_elemento(self, raiz, elemento):
        if raiz == None:
            raiz = No()
            raiz.elemento = elemento
        else:
            numero_do_filho = randint(0, 4)

            if numero_do_filho == 0:
                raiz.filho1 = self.inserir_elemento(raiz.filho1, elemento)
            elif numero_do_filho == 1:
                raiz.filho2 = self.inserir_elemento(raiz.filho2, elemento)
            elif numero_do_filho == 2:
                raiz.filho3 = self.inserir_elemento(raiz.filho3, elemento)
            elif numero_do_filho == 3:
                raiz.filho4 = self.inserir_elemento(raiz.filho4, elemento)
            elif numero_do_filho == 4:
                raiz.filho5 = self.inserir_elemento(raiz.filho5, elemento)
        return raiz

    def navegação(self, raiz, espaco):
        if raiz != None:
            print(f'{espaco}({str(raiz.elemento)})')
            self.navegação(raiz.filho1, espaco + 'f1 ->')
            self.navegação(raiz.filho2, espaco + 'f2 ->')
            self.navegação(raiz.filho3, espaco + 'f3 ->')
            self.navegação(raiz.filho4, espaco + 'f4 ->')
            self.navegação(raiz.filho5, espaco + 'f5 ->')


if __name__ == "__main__":
    raiz = No()
    raiz.elemento = 1
    raiz = raiz.inserir_elemento(raiz, 2)
    raiz = raiz.inserir_elemento(raiz, 3)
    raiz = raiz.inserir_elemento(raiz, 4)
    raiz = raiz.inserir_elemento(raiz, 5)
    raiz = raiz.inserir_elemento(raiz, 6)
    raiz = raiz.inserir_elemento(raiz, 7)
    raiz = raiz.inserir_elemento(raiz, 8)
    raiz = raiz.inserir_elemento(raiz, 9)
    raiz = raiz.inserir_elemento(raiz, 10)
    raiz = raiz.inserir_elemento(raiz, 11)
    raiz = raiz.inserir_elemento(raiz, 12)
    raiz = raiz.inserir_elemento(raiz, 13)
    raiz = raiz.inserir_elemento(raiz, 14)
    raiz = raiz.inserir_elemento(raiz, 15)
    raiz = raiz.inserir_elemento(raiz, 16)

    raiz.navegação(raiz, '')


