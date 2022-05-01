class PessoaFisica:
    def __init__(self, nome:str, idade:int, altura:float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def diga_ola(self):
        print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} anos e minha altura é {self.altura}m.')

    def cozinha(self, receita:str):
        print(f'Estou cozinhado um(a): {receita}')

    def andar(self, distancia:float):
        print(f'Saí para andar. Volto quando completar {distancia} metros')

#Instanciar um objeto da classe PessoaFisica
pessoa = PessoaFisica(nome='Ariana', idade=27, altura=1.75)

#Chama os metodos dentro da classe "PessoaFisica"
pessoa.diga_ola()
pessoa.cozinha('Feijão')
pessoa.andar(750.9)