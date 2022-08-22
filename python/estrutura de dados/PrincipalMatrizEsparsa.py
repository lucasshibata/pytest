from DiretorDeMatrizEsparsa import DiretorDeMatrizEsparsa

cabeca = DiretorDeMatrizEsparsa(0, None, None)

cabeca = DiretorDeMatrizEsparsa.inserir(cabeca, 1)
cabeca = DiretorDeMatrizEsparsa.inserir(cabeca, 2)
cabeca = DiretorDeMatrizEsparsa.inserir(cabeca, 3)
cabeca = DiretorDeMatrizEsparsa.inserir(cabeca, 16)
cabeca = DiretorDeMatrizEsparsa.inserir(cabeca, 32)
cabeca = DiretorDeMatrizEsparsa.inserir(cabeca, 33)

cabeca.imprimirMatrizEsparsa(cabeca)