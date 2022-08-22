from ex13 import *

if __name__ == "__main__":
    p1 = Professor('Alice',0,5)
    p2 = Professor('Carmem', dependente=0, qtd_turma=2)
    p3 = Professor('wilson')
    p4 = Funcionario('Julio')
    print(p1.get_nome())
    print(p2.get_dependente())
    print(p3.get_qtd_turma())
    p1.get_rendimento()
    p2.salario_total()
    print(Pessoa.get_qtd_professor())