class Funcionario:
    def __init__(self, cpf, nome, salario):
        self.cpf = cpf
        self.nome = nome
        self.salario = salario 
    

    def set_cpf(self, novo_cpf):
        self.cpf = novo_cpf
    
    def get_cpf(self):
        return self.cpf

    def set_nome(self, novo_nome):
        self.nome = novo_nome
    
    def get_nome(self):
        return self.nome
    
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    
    def get_salario(self):
        return self.salario

    def __str__(self):
        s1 = f'nome: {self.nome}, cpf: {self.cpf}, salario: R${self.salario:.2f}'
        return s1

    def bonificacao(self):
        return self.salario + self.salario *10/100


class Gerente(Funcionario):
    def __init__(self, cpf, nome, salario, senha, qtd_gerencia):
        super().__init__(cpf, nome, salario)
        self.senha = senha
        self.qtd_gerencia = qtd_gerencia

    def set_senha(self, nova_senha):
        self.senha = nova_senha
    
    def get_senha(self):
        return self.senha
    
    def set_qtd_gerencia(self, nova_qtd_gerencia):
        self.qtd_gerencia = nova_qtd_gerencia
    
    def get_qtd_gerencia(self):
        return self.qtd_gerencia

    def __str__(self):
        s1 = super().__str__()
        s = f'{s1}, qtd: {self.qtd_gerencia}'
        return s

    def verifica_senha(self):
        senha = int(input('Digite a senha do gerente 1: '))
        if senha == self.senha:
            return 'acesso concedido'
        else:
            return 'acesso negado'

    def bonificacao(self):
        self.salario += self.salario *20/100
        return self.salario
        

if __name__ == "__main__":
    funcionario1 = Funcionario('04674924502', 'Lucas', 13000)
    print(f'{funcionario1}')
    gerente1 = Gerente('546541484548', 'MAtheus', 26000, 123456, 23)
    print(f'{gerente1.__str__()}')
    print(f'{gerente1.verifica_senha()}')
    print(f'{gerente1.bonificacao()}')
    oi = vars(gerente1)
    print(f'{oi.index("cpf")}')
    print(f'{gerente1.__dict__}')