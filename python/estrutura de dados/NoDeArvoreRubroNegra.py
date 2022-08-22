class NoDeArvoreRubroNegra:
    def __init__(self):
        self.valor = 0
        self.vermelho = True
        self.filhoEsquerdo = None
        self.filhoDireito = None

    def buscarElemento(raiz, valor, caminho):
        if (raiz == None):
            print("Não encontrei o elemento !")
        elif (raiz.valor == valor):
            print("Encontrei " + str(valor) + ": " + caminho)
        else:
            if (raiz.valor > valor):
                NoDeArvoreRubroNegra.buscarElemento(raiz.filhoEsquerdo, valor, caminho + "esquerda, ")
            else:
                NoDeArvoreRubroNegra.buscarElemento(raiz.filhoDireito, valor, caminho + "direita, ")

    def inserirElemento(raiz, valor):
        if (raiz == None):
            raiz = NoDeArvoreRubroNegra()
            raiz.valor = valor
        else:
            if (raiz.valor > valor):
                raiz.filhoEsquerdo = NoDeArvoreRubroNegra.inserirElemento(raiz.filhoEsquerdo, valor)
            else:
                raiz.filhoDireito = NoDeArvoreRubroNegra.inserirElemento(raiz.filhoDireito, valor)

            if (raiz.filhoDireito != None and raiz.filhoEsquerdo != None):
                if ((raiz.filhoDireito.vermelho == True) and (raiz.filhoEsquerdo.vermelho == False)):
                    raiz = NoDeArvoreRubroNegra.rotacionarAEsquerda(raiz)

            if (raiz.filhoEsquerdo != None and raiz.filhoEsquerdo.filhoEsquerdo != None):
                if ((raiz.filhoEsquerdo.vermelho == True) and (raiz.filhoEsquerdo.filhoEsquerdo.vermelho == True)):
                    raiz = NoDeArvoreRubroNegra.rotacionarADireita(raiz)

            if (raiz.filhoEsquerdo != None and raiz.filhoDireito != None):
                if ((raiz.filhoEsquerdo.vermelho == True) and (raiz.filhoDireito.vermelho == True)):
                    raiz = NoDeArvoreRubroNegra.subirVermelho(raiz)

        return raiz
    
    def rotacionarAEsquerda(raiz):
        x = raiz.filhoDireito
        raiz.filhoDireito = x.filhoEsquerdo
        x.filhoEsquerdo = raiz
        x.vermelho = raiz.vermelho
        raiz.vermelho = True
        return x

    def rotacionarADireita(raiz):
        x = raiz.filhoEsquerdo
        raiz.filhoEsquerdo = x.filhoDireito
        x.filhoDireito = raiz
        x.vermelho = raiz.vermelho
        raiz.vermelho = True
        return x

    def subirVermelho(raiz):
        raiz.vermelho = True
        raiz.filhoEsquerdo.vermelho = False
        raiz.filhoDireito.vermelho = False
        return raiz
	
    def navegar(raiz):
        if (raiz != None):
            NoDeArvoreRubroNegra.navegar(raiz.filhoEsquerdo)
            print(raiz.valor, end = ", ")
            NoDeArvoreRubroNegra.navegar(raiz.filhoDireito)