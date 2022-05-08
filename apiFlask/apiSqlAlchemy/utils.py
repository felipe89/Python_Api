from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome="Jady", idade=7)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    # pessoa = Pessoas.query.filter_by(nome="Jady").first()
    # print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Jady').first()
    pessoa.nome = 'Carol'
    pessoa.idade = 28
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Ariana").first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()