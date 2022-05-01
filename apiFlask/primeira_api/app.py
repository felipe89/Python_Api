#Para iniciar a criação de uma api com FLASK é necessário efetuar o importe da mesma certificando que o flask esteja instalado
# Ao informar o junto ao import do Flask o comando jsonify permite que devolvemos a informação e padrão json conforme passado no return
from flask import Flask, jsonify, request
import json

# A annotation 'app.route('/')' define a rota que a sua aplicação ira chamar. quando o parametro da rota é informado '<int:id>' isso siginifica que estamos tipando a rota a mesma só será infomando atraves do id e se não estiver nada (/) retornara de qlqr forma
app = Flask(__name__)
@app.route('/<int:id>')
def pessoas(id):
    return jsonify({'id': id, 'nome': 'Felipe', 'profissao': 'Desenvolvedor', 'idade': 32})

#Informando mais de um parametro na app.route()
# @app.route('/soma/<int:valor1>/<int:valor2>/')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1 + valor2})

# Definindo methods via requisição post para implementar uma soma para fazer esse metodo abaixo funcionar precimas importar o json no inicio da classe
# o request para definir a leitura do body no postman
@app.route('/soma', methods=['POST', 'PUT', 'GET'])
def soma():

    #Se for um POST a requisição utilizada os valores de soma dentro do body
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    # Sen não e for um GET na requisição no postman efetuara a soma abaixo no postman
    elif request.method == 'GET':
        total = 10 + 10

    return jsonify({'soma': total})

# Atalho para criação do metodo if abaixo escreva a palavra 'main' e o restando ela autocompletara conforme abaixo
# Sem esquecer do parametro 'debug=True' para restatar a aplicação após qlqr atualização.
if __name__ == '__main__':
    app.run(debug=True)