class Pessoa:
    def __init__(self, nome='', sobrenome='', idade=1):
        self.idade = idade
        if idade <=0:
            print('idade inválida!')
            self.idade = 1
        elif idade > 150:
            print('idade inválida!')
            self.idade = 1
        self.nome = nome
        self.sobrenome = sobrenome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_nome(self):
        return self.nome

    def set_sobrenome(self, novo_sobrenome):
        self.sobrenome = novo_sobrenome

    def get_sobrenome(self):
        return self.sobrenome

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def get_idade(self):
        return self.idade

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}' 
    
    def __str__(self):
        s = f'{self.nome_completo()}, {self.get_idade()}'
        return s

    def mais_velho(self, pessoa):
        if self.idade > pessoa.idade:
            print(f'{self.nome} é a mais velha')
        elif pessoa.idade > self.idade:
            print(f'{pessoa.nome} é mais velha ')

if __name__ == "__main__":
    pessoa1 = Pessoa('Lucas', 'Shibata', 19)
    pessoa2 = Pessoa('Adilson', 'Fernandes', 32)
    pessoa3 = Pessoa('Maria')

    print(f'{pessoa1.get_nome()}')
    print(f'{pessoa2.get_nome()}')
    print(f'{pessoa1.get_idade()}')
    print(f'{pessoa2.get_idade()}')
    print(f'{pessoa1.get_sobrenome()}')
    print(f'{pessoa2.get_sobrenome()}')

    pessoa2.set_nome('Julia')
    pessoa2.set_idade(18)
    pessoa2.set_sobrenome('Guimarães')

    print('')
    print('-='*15)
    print(f'{pessoa2.get_nome()}')
    print(f'{pessoa2.get_idade()}')
    print(f'{pessoa2.get_sobrenome()}')

    print('')
    print('-='*15)
    print(f'{pessoa1.nome_completo()}')
    print(f'{pessoa2.nome_completo()}')
    print(f'{pessoa3.nome_completo()}')

    print('')
    print('-='*15)
    print(f'{pessoa1.__str__()}')


    pessoa2.mais_velho(pessoa1)
