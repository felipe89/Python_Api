from flask_restful import Resource, request
import json


lista_habilidades = [
        {'id': 0,
         'nome_habilidade': 'Python'
         },
        {'id': 1,
         'nome_habilidade':'PHP',
         },
        {'id': 2,
         'nome_habilidade' : 'Node'
         }
]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados
    
