
class Veiculo:
    def __init__(self, valor=0, modelo='', quilometragem=0):
        self.valor = valor
        self.modelo = modelo
        self.quilometragem = quilometragem

    def set_valor (self, novo_valor):
        self.valor = novo_valor
    def get_valor (self):
        return self.valor

    def set_modelo (self, novo_modelo):
        self.modelo = novo_modelo 
    def get_modelo (self):
        return self.modelo

    def set_quilometragem (self, nova_quilometragem):
        self.quilometragem = nova_quilometragem
    def get_quilometragem (self):
        return self.quilometragem

    def atualizar_valor(self, diferenca):
        self.valor += diferenca

    def atualizar_valor_pct(self, porcentagem):
        self.valor = self.valor + self.valor*porcentagem/100

    def zero(self):
        if self.quilometragem == 0:
            print('Veiculo zerado')
        else:
            print('veiculo usado')


class Carro(Veiculo):
    def __init__(self, valor=0, modelo='', quilometragem=0, qtd_portas=0):
        super().__init__(valor, modelo, quilometragem)
        self.qtd_portas = qtd_portas

    def set_qtd_portas (self, nova_qtd_portas):
        self.qtd_portas = nova_qtd_portas
    def get_qtd_portas (self):
        return self.qtd_portas

    def __str__(self):
        s = f'valor: {self.valor}, modelo: {self.modelo}, quilometragem: {self.quilometragem}, qtd_portas: {self.qtd_portas}'
        return s

class Moto(Veiculo):
    def __init__(self, valor=0, modelo='', quilometragem=0, cilindradas=0):
        super().__init__(valor, modelo, quilometragem)
        self.cilindradas = cilindradas

    def set_cilindradas (self, nova_cilindradas):
        self.cilindradas = nova_cilindradas
    def get_cilindradas (self):
        return self.cilindradas

    def __str__(self):
        s = f'valor: {self.valor}, modelo: {self.modelo}, quilometragem: {self.quilometragem}, cilindrada: {self.cilindradas}'
        return s

if __name__ == "__main__":
    carro1 = Carro(1700000, 'Tesla model S', 30, 4)
    moto1 = Moto(94900, 'Harley Davison x80', 40, 1746)

    print(f'{carro1.__str__()}')
    print(f'{moto1.__str__()}')
    valor = moto1.__dict__["valor"]
    print(f'{valor}')
    carro1.atualizar_valor(212313)
    print(f'{carro1.get_valor()}')
    carro1.zero()
     