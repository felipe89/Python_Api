class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_like(self):
        self.likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes += 1


vingadores = Filme('Spider-man', 2022, 160)
vingadores.dar_like()

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Tempo: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('Atlanta', 2019, 2)
atlanta.dar_like()

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporada: {atlanta.temporadas} - Likes: {atlanta.likes}')

