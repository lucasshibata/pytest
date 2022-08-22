'''# programação orientada a objeto:

class Aluno:  #primeira letra de cada palavra maiuscula, sem sublinhado
    def __init__(self , [parametro_1, parametro_2]): #método contrutor
        self.atributo_1 = valor_inicial ou parametro_1
        self.atributo_2 = valor_inicial ou parametro_2
        pass

    def outro_metodo(self): #método
        self.x = 0
        self.y = 0
        pass

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
        return self.x, self.y

if __name__ == "__main__":
    p = Point()'''

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class Aluno:
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_mensalidade(self):
        return self.mensalidade
    
    def set_mesalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade

    def get_idade(self):
        return self.idade
    
    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def aumento_mensalidade(self, aumento):
        self.mensalidade += aumento    

    def aumento_mensalidade_porcentagem(self, porcentagem):
        self.mensalidade += self.mensalidade * porcentagem/100

    @property
    def get_all(self):
        return self.nome, self.mensalidade, self.idade

if __name__ == "__main__":
    aluno1 = Aluno('Paulo', 1100.00, 21)
    aluno2 = Aluno('Carla', 900.00, 20)
    print('-='*15)
    print(f'nome: {aluno1.get_nome()}')
    print(f'mensalidade: R${aluno1.get_mensalidade():.2f}')
    print(f'idade: {aluno1.get_idade()}')
    print('-='*15)
    print('-='*15)
    count = 0
    for c in aluno2.get_all:
        count += 1
        if count == 1:
            print(f'nome: {c}')
        if count == 2:
            print(f'mensalidade: {c}')
        if count == 3:
            print(f'idade: {c}')
    print('-='*15)
    aluno2.aumento_mensalidade(100)
    aluno1.aumento_mensalidade_porcentagem(10)
    print(f'mensalidade: R${aluno1.get_mensalidade():.2f}')
    print(f'mensalidade: R${aluno2.get_mensalidade():.2f}')