class Carro:
    def __init__(self, marca:str, modelo:str, ano:int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def saldacao(self):
        print(f'Olá meu carro é da {self.marca}, é um {self.modelo} de ano {self.ano}')

carro = Carro("Ford", "CrossOver", 2015)
carro.saldacao()