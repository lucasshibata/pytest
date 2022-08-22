# propriedades da classe 

class No:
    def __init__(self):
        self.numero = 0
        self.proximo = None

    def inserirElementoNaLista(primeiro, elemento):
        if (primeiro == None):
            primeiro = elemento
        else:
            ponteiro = primeiro
            while(ponteiro.proximo != None):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = elemento
        return primeiro

    def mostrarLista(primeiro):
        ponteiro = primeiro 
        while (ponteiro != None):
            print (ponteiro.numero)
            ponteiro = ponteiro.proximo

    def excluirElementoDaLista(primeiro, numeroASerExcluido):
        ponteiro = None
        if primeiro.numero == numeroASerExcluido:
            primeiro = primeiro.proximo
        else:
            ponteiro = primeiro
            while ponteiro.proximo != None:
                if ponteiro.proximo.numero == numeroASerExcluido:
                    ponteiro.proximo = ponteiro.proximo.proximo
                ponteiro = ponteiro.proximo
                if ponteiro == None:
                    break
        return primeiro
        

'''primeiro = None
elemento = No()
elemento.numero = 3
primeiro = No.inserirElementoNaLista(primeiro, elemento)

primeiro.mostrarLista()'''
