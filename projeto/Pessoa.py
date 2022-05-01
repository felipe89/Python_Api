class Pessoa:
    pass


class Pessoa:

#Construitor
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo

#Metodo
    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso!")

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

#Conficional simples
if __name__ == "__main__":
    pessoa1 = Pessoa("Felipe", "M", "320.225.852.77,", True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pessoa1.ativo)

#Utilizando geters e setters
    pessoa1.set_nome("Jady")
    print(pessoa1.get_nome())

# Utilizando properties
    pessoa1.nome = "Jady"
    print(pessoa1.nome)
    
