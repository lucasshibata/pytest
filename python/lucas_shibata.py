'''1. Crie uma classe com o método construtor e pelo menos dois atributos.
2. Crie os métodos gets e sets dos atributos.
3. Crie pelo menos um método funcional.
4. No método main, teste (use) a classe criada, crie pelo menos dois objetos dessa classe e use todos os métodos desenvolvidos na classe.'''

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Produtos:
    def __init__(self, identidade, preco):
        self.identidade = identidade
        self.preco = preco

    def set_identidade(self, nova_identidade):
        self.identidade = nova_identidade
    
    def get_identidade(self):
        return self.identidade

    def set_preco(self, novo_preco):
        self.preco = novo_preco
    
    def get_preco(self):
        return self.preco

    def devolve_dados(self):
        return self.identidade, self.preco

    def soma_dois_produtos(self, produto):
        return self.preco + produto.preco

if __name__ == "__main__":
    produto1 = Produtos('sabonete', 3.39)
    produto2 = Produtos('pasta_de_dente', 4.70)
    print(f'{produto1.get_preco()}')
    print(f'{produto2.get_preco()}')
    print(f'{produto1.devolve_dados()}')
    print(f'{produto1.soma_dois_produtos(produto2)}')