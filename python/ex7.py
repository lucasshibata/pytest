class Veiculo:
    def __init__(self, modelo, ano=0, valor=0):
        
        self.modelo = modelo
        if ano > 0:
            self.ano = ano
        else:
            self.ano = 0

        if valor > 0:
            self.valor = valor
        else:
            self.valor = 0

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, nome_modelo):
        try:
            self.modelo = str(nome_modelo)
        except:
            self.modelo = ''

    def get_ano(self):
        return self.ano

    def set_ano(self, novo_ano):
        try:
            self.ano = int(novo_ano)
        except:
            self.ano = 0                                                                                                        #                                          OwO
    
    def get_valor(self):
        return self.valor

    def set_valor(self, novo_valor):
        try:
            self.valor = float(novo_valor)
        except:
            self.valor = 0

    def mostra_dados(self):
        qualquer = str(f'R$ {self.valor:.2f}')
        dados = f'{self.modelo}, {self.ano}, {qualquer}'.strip("()'").replace("'", '')
        return dados

    def compara_valor(self, carro2):
        if self.valor == carro2.valor:
            print('Tem o mesmo valor')
        elif self.valor > carro2.valor:
            print(f'{self.valor} é maior que {carro2.valor}')
        else:
            print(f'{self.valor} é menor que {carro2.valor}')

    def compara_valor2(self, carro2):
        if self.valor == carro2.valor:
            print('Tem o mesmo valor')
        elif self.valor > carro2.valor:
            print(f'{self.valor} é maior que {carro2.valor}')
            print(f'{self.mostra_dados}')
        else:
            print(f'{self.valor} é menor que {carro2.valor}')
            print(f'{carro2.mostra_dados()}')
 

if __name__ == "__main__":
    carro1 = Veiculo('lamborghini veneno', 2021, 10500000)
    carro2 = Veiculo('bugatti divo', 2020, 1203000)

    print(f'{carro1.mostra_dados()}')
    print(f'{carro2.mostra_dados()}')

    carro1.set_modelo('honda city')
    carro1.set_ano(2022)
    carro1.set_valor(120300)
    text = f'{carro1.mostra_dados()}'
    print(f'{text}')

    carro4 = Veiculo('Argo')
    print(f'{carro4.mostra_dados()}')
    carro1.compara_valor2(carro2)
    