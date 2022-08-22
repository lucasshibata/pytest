'''1. Crie uma superclasse com o método construtor e pelo menos um atributo.

2. Crie pelo menos um método get e um método set do atributo da superclasse.

3. Crie pelo menos um método funcional na superclasse.

4. Crie duas subclasses que herdam da superclasse com o método construtor e pelo menos dois atributos.

5. Crie pelo menos um método get e um método set dos atributos das duas superclasses.

6. Em uma das subclasses sobrescreva um método da superclasse

7. No método main, teste (use) as classes criadas, crie pelo menos um objeto de cada subclasse.

8. E teste (use) todos os métodos desenvolvidos nas classes.

Obs.: crie as classes e os métodos funcionais diferentes dos desenvolvidos durante as aulas.'''

# -=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=
class Animal:
    def __init__(self, nome='', cor='', tamanho=0):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_nome(self):
        return self.nome

    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def get_cor(self):
        return self.cor

    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def get_tamanho(self):
        return self.tamanho

    def verificar_tamanho(self):
        if self.tamanho <= 0:
            print(f'tamanho inválido')
            self.tamanho = 0
        else:
            print(f'tamanho válido')


class Gato(Animal):
    def __init__(self, nome, cor, tamanho, raca=''):
        super().__init__(nome, cor, tamanho)
        self.raca = raca
        
    def set_raca (self, nova_raca):
        self.raca = nova_raca

    def get_raca (self):
        return self.raca

    def __str__(self):
        s = f'nome: {self.nome}, cor: {self.cor}, tamanho: {self.tamanho}, raca: {self.raca}'
        return s


class Cachorro(Animal):
    def __init__(self, nome, cor, tamanho, pedigree=''):
        super().__init__(nome, cor, tamanho)
        self.pedigree = pedigree
    
    def set_pedigree (self, novo_pedigree):
        self.pedigree = novo_pedigree

    def get_pedigree (self):
        return self.pedigree

    def __str__(self):
        s = f'nome: {self.nome}, cor: {self.cor}, tamanho: {self.tamanho}, pedigree: {self.pedigree}'
        return s
        

if __name__ == "__main__":
    gato1 = Gato('Jinx', 'marrom', 0.75, 'sphynx')
    cachorro1 = Cachorro('Thor', 'branco', 0.53, 'Husky')

    print(cachorro1.__str__())
    print(gato1.__str__())

    cachorro1.set_nome('Luke')
    cachorro1.set_pedigree('Golden retriever')

    print(cachorro1.get_nome())
    print(cachorro1.get_pedigree())

    gato1.set_tamanho(0.87)
    gato1.set_raca('persa')

    print(gato1.get_tamanho())
    print(gato1.get_raca())

    gato1.verificar_tamanho()