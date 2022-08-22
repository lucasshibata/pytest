import datetime
class Pessoa(object):
    def __init__(self, nome='', peso=0, altura=0, dta_nasci=datetime.date.today()):
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.dta_nasci = dta_nasci

    def set_nome(self, novo_nome):
        if type(novo_nome) == type(str()):
            self.nome = novo_nome
        else:
            print('tipo inválido')

    def get_nome(self):
        return self.nome

    def set_peso(self, novo_peso):
        self.peso = novo_peso

    def get_peso(self):
        return self.peso

    def set_altura(self, nova_altura):
        self.altura = nova_altura

    def get_altura(self):
        return self.altura

    def set_dta_nasci (self, nova_dta_nasci):
        self.dta_nasci = nova_dta_nasci

    def get_dta_nasci(self):
        return self.dta_nasci

    def get_idade(self):
        atual = datetime.date.today()
        dia = atual.day
        mes = atual.month
        ano = atual.year
        idade = ano - self.dta_nasci.year
        if mes < self.dta_nasci.month:
            idade -= 1
            return f'{idade} anos'
        elif mes == self.dta_nasci.month:
            if dia < self.dta_nasci.day:
                idade -= 1
                return f'{idade} anos'
            elif dia >= self.dta_nasci.day:
                return f'{idade} anos'
        else: 
            return f'{idade} anos'
        
    def get_all(self):
        data = f'{self.dta_nasci.day}/{self.dta_nasci.month}/{self.dta_nasci.year}'
        return f'{self.nome}, {self.peso}Kg, {self.altura:.2f} m, {data}'

    def calc_imc(self):
        imc = self.peso/self.altura**2
        if imc < 18.5:
            return f'seu imc é: {imc:.2f}, está abaixo do peso'
        if imc >= 18.5 and imc < 25:
            return f'seu imc é: {imc:.2f}, está ideal'
        if imc >= 25 and imc < 30:
            return f'seu imc é: {imc:.2f}, está com sobrepeso'
        if imc >= 30 and imc < 35:
            return f'seu imc é: {imc:.2f}, está obeso I'
        if imc >= 35 and imc < 40:
            return f'seu imc é: {imc:.2f}, está obeso II'
        if imc >= 40:
            return f'seu imc é: {imc:.2f}, está obeso III'


def data(ano, mes, dia):
    data = datetime.date(ano, mes, dia)
    return data

if __name__ == "__main__":
    pessoa1 = Pessoa('Lucas', 61, 1.62, data(2002, 12, 30))
    pessoa2 = Pessoa('Matheus', 62, 1.82, data(2001, 9, 11))
    pessoa3 = Pessoa('Marcos', 65, 1.80, data(2003, 1, 16))
    pessoa4 = Pessoa('kauã', 70, 1.82, data(2003, 5, 18))


    print(f'{pessoa3.get_dta_nasci()}')
    print(f'{pessoa1.get_idade()}')
    print(f'{pessoa1.get_all()}')
    print(f'{pessoa2.calc_imc()}')