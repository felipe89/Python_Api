# Estrutura de classes e objetos
class Pessoa:

    # Metodo construtor da classe
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade = Idade

    def Boas_vinda(self):
        print('Olá seja Bem vindo!', self.Nome)

    def Recusado(self):
        print('Seu Acesso foi recusado!')

    # Função
    def Maior_idade(self):
        if self.Idade >= 18:
            print('Usuário é maior de idade!')
            self.Boas_vinda()
        else:
            print('Usuário é menor de idade!')
            self.Recusado()

            # Chamada da função Pessoa
            Dados = Pessoa('Felipe', 10)
            print(Dados)

#Print Formatado
print('Soma de 2 + 2 é: ', 2 + 2 )
print(f'Soma de 2 + 2 é:  {2 + 2}')
print('Soma de 2 + 2 é: {}' .format(2+2))