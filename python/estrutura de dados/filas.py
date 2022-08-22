# FIFO (first in - first out)
class NoDeFila:
    def __init__(self, numero):
        self.numero = numero
        self.proximo = None


    '''def inserirElementoNaLista(primeiro, elemento):
        if (primeiro == None):
            primeiro = elemento
        else:
            ponteiro = primeiro
            while(ponteiro.proximo != None):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = elemento
        return primeiro'''


    '''def mostrarLista(primeiro):
        ponteiro = primeiro 
        while (ponteiro != None):
            print (ponteiro.numero)
            ponteiro = ponteiro.proximo'''


    '''def excluirElementoDaLista(primeiro, numeroASerExcluido):
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
        return primeiro'''
    

    def inserirElementoNaFila(fila, elemento):
        ponteiro = None
        if fila == None:
            fila = elemento
        else:
            ponteiro = fila
            while (ponteiro.proximo != None):
                ponteiro = ponteiro.proximo
            ponteiro.proximo = elemento
        return fila
        

    def inserirElementoNaFilaRecursivamente(self, fila, elemento):
        if fila == None:
            fila = elemento
        elif fila.proximo == None:
            fila.proximo = elemento
        else:
            self.inserirElementoNaFilaRecursivamente(fila.proximo,elemento)
        return fila


    def removerElementoDaFila(fila):
        if fila == None:
            print('Não há elementos para ser removidos!')
        else:
            print(f'Removi um elemento: {fila.numero}')
            fila = fila.proximo
        return fila
    

    def listarFila(fila):
        ponteiro = None
        posicao = 1
        ponteiro = fila
        while (ponteiro != None):
            print(f'{posicao}º elemento da fila: {ponteiro.numero}')
            posicao +=1
            ponteiro = ponteiro.proximo


    def listarFilaRecursivamente(self, fila):
        if fila != None:
            print(f'elemento da fila: {fila.numero}')
            self.listarFilaRecursivamente(fila.proximo)


if __name__ == "__main__":
    fila = None
    '''fila = NoDeFila.inserirElementoNaFila(fila, NoDeFila(1))
    fila = NoDeFila.inserirElementoNaFila(fila, NoDeFila(10))
    fila = NoDeFila.inserirElementoNaFila(fila, NoDeFila(100))
    NoDeFila.listarFila(fila)
    fila = NoDeFila.removerElementoDaFila(fila)
    NoDeFila.listarFila(fila)'''
    fila = NoDeFila.inserirElementoNaFilaRecursivamente(fila, fila, NoDeFila(20))
    fila = NoDeFila.inserirElementoNaFilaRecursivamente(fila, fila, NoDeFila(200))
    fila = NoDeFila.inserirElementoNaFilaRecursivamente(fila, fila, NoDeFila(2000))
    NoDeFila.listarFilaRecursivamente(fila, fila)
    fila = NoDeFila.removerElementoDaFila(fila)
    NoDeFila.listarFilaRecursivamente(fila, fila)