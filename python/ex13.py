class Pessoa(object):
    qtd_professores = 0
    def __init__(self, nome='', dependente=0):
        self.nome = nome
        self.dependente = dependente
        Pessoa.qtd_professores +=1

    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        if isinstance(self.nome, str):
            self.nome = novo_nome

    def get_dependente(self):
        return self.dependente
    def set_dependente(self, novo_dependente):
        if isinstance(self.dependente, int):
            self.dependente = novo_dependente
    @classmethod
    def get_qtd_professor(cls):
        return Pessoa.qtd_professores


class Professor(Pessoa):
    def __init__(self, nome='', dependente=0, qtd_turma=0):
        super().__init__(nome, dependente)
        self.qtd_turma = qtd_turma

    def get_qtd_turma(self):
        return self.qtd_turma
    def set_qtd_turma(self, nova_qtd):
        self.qtd_turma = nova_qtd
    def get_rendimento(self):
        print('oi')
        rendimento = self.qtd_turma * 300
        print(f'esse professor trabalha em {self.qtd_turma} e recebe {rendimento} de salario')
    def salario_total(self):
        salario = self.qtd_turma*300 + self.dependente*100
        print(f'salario total é de {salario}')


class Funcionario(Pessoa):
    def __init__(self, nome='', dependente=0, salario_fixo=0):
        super().__init__(nome, dependente)
        self.salario_fixo = salario_fixo

    def get_salario_fixo(self):
        return self.salario_fixo
    def set_salario_fixo(self, novo_salario):
        self.salario_fixo = novo_salario


''' if qtd_turma >= 0:
 else:
            print('Erro quantidade inválida')'''