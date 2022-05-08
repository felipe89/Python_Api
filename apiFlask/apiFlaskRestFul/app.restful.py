from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

# Lista estatica para manipulação de dados sem banco de dados
desenvolvedores = [
    {
        'id':0,
         'Nome': 'Felipe',
         'Habilidade': ['Python', 'Flask']
     },
    {
        'id':1,
        'Nome': 'Jady',
        'Habilidades': ['Java', 'Typescript']
     },
    {
        'id':2,
        'Nome': 'Ariana',
        'Habilidade': ['Javascript', 'Angular']
     }
]

#Devolve um desenvovedor pelo id, também altera e deleta um desenvolvedor por id
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolverdo de ID {} não existe mais na lista!'.format(id)
            response = {'status': 'Error!', 'mensagem': mensagem}
        except Exception:
            error = 'Erro desconhecido. Procure o administrado!'
            response = {'status': 'Error!', 'mensagem': error}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Status': 'Sucesso!', 'mensagem': 'Registro Excluido'}


# lista todos os desenvolvedores, e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


#Informando as rotas que estamos passando para cada requisição
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,  '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>/')



if __name__ == '__main__':
    app.run(debug=True)