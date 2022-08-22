from NoDeMatrizEsparsa import NoDeMatrizEsparsa

class DiretorDeMatrizEsparsa:
    def __init__(self, resto, proximoNo, proximoDiretor):
        self.resto = resto
        self.proximoNo = proximoNo
        self.proximoDiretor = proximoDiretor

    def inserir(matrizEsparsa, numero):
        resto = (numero % 16)
        ponteiroDiretor = matrizEsparsa

        while (ponteiroDiretor != None):
            if (ponteiroDiretor.resto == resto):
                novoNo = NoDeMatrizEsparsa(numero, ponteiroDiretor.proximoNo)
                ponteiroDiretor.proximoNo = novoNo
                break

            ponteiroDiretor = ponteiroDiretor.proximoDiretor

        if (ponteiroDiretor == None):
            novoNo = NoDeMatrizEsparsa(numero, None)

            matrizEsparsa = DiretorDeMatrizEsparsa(resto, novoNo, matrizEsparsa)
		
        return matrizEsparsa
	
    def imprimirMatrizEsparsa(self, matrizEsparsa):
        ponteiroDiretor = matrizEsparsa

        while (ponteiroDiretor != None):
            ponteiroNo = ponteiroDiretor.proximoNo

            linha = str(ponteiroDiretor.resto) + "\t"

            while (ponteiroNo != None):
                linha += str(ponteiroNo.numero) + "\t"
                ponteiroNo = ponteiroNo.proximo

            print(linha)

            ponteiroDiretor = ponteiroDiretor.proximoDiretor