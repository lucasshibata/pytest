class ContaCorrente(object):
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        qtd_conta = 0
    @classmethod
    def get_qtd_contas(cls):
        return ContaCorrente.qtd_conta
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_nome (self):
        return self.nome

    def set_saldo (self, novo_saldo):
        self.saldo = novo_saldo
    def get_saldo (self):
        return self.saldo

    def __str__(self):
        s = f'nome: {self.nome}, saldo: R${self.saldo:.2f}'
        return s

    def deposito(self, valor):
        self.saldo += valor
        return f'saldo atualizado: {self.saldo}'


class PessoaFisica(ContaCorrente):
    def __init__(self, nome, saldo, genero, cpf):
        super().__init__(nome, saldo)
        self.genero = genero
        self.cpf = cpf

    def set_genero (self, novo_genero):
        self.genero = novo_genero
    def get_genero (self):
        return self.genero

    def set_cpf (self, novo_cpf):
        self.cpf = novo_cpf
    def get_cpf (self):
        return self.cpf

    def __str__(self):
        s = super().__str__() + f', genero: {self.genero}, cpf: {self.cpf}'
        return s

    def retirada(self, valor):
        self.saldo -= (valor + 2)
        return f'saldo atualizado: {self.saldo}'


class PessoaJuridica(ContaCorrente):
    def __init__(self, nome, saldo, modalidade, cnpj):
        super().__init__(nome, saldo)
        self.modalidade = modalidade
        self.cnpj = cnpj

    def set_modalidade (self, nova_modalidade):
        self.modalidade = nova_modalidade
    def get_modalidade (self):
        return self.modalidade

    def set_cnpj (self, novo_cnpj):
        self.cnpj = novo_cnpj
    def get_cnpj (self):
        return self.cnpj

    def __str__(self):
        s = super().__str__() + f', modalidade: {self.modalidade}, cnpj: {self.cnpj}'
        return s

    def retirada(self, valor):
        self.saldo -= (valor + 5)
        return f'saldo atualizado: {self.saldo}'


if __name__=="__main__":
    pessoa1 = PessoaFisica('caio', 50000, 'masculino', '7862866845')
    print(pessoa1.__str__())
    print(pessoa1.__dict__)
    print(vars(pessoa1))
    print(pessoa1.deposito(11000))
    print(pessoa1.retirada(500))
    print(f'qtd. contas', ContaCorrente.get_qtd_contas())