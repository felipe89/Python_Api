from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolverdo de ID {} não existe mais na lista!'.format(id)
            response = {'status': 'Error!', 'mensagem': mensagem}
        except Exception:
            error = 'Erro desconhecido. Procure o administrado!'
            response = {'status': 'Error!', 'mensagem': error}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method =='DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido!'})

# lista todos os desenvolvedores, e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


if __name__ == '__main__':
    app.run(debug=True)