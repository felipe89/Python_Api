from flask import Flask

app = Flask(__name__)

# Dentro do parametro podemos  utilizar duas maneira como metodo de requisição o "POST" e o "GET" conforme exemplo
# Tambem atraves da uri podemos passar diversos paramentros conforme exemplo:
@app.route("/<numero>", methods=['POST', 'GET'])
def hello(numero):
    return u'Olá Mundo! {}'.format(numero) # com o paramentro ajustado via uri navegador apresentando "http://127.0.0.1:5000/10" 

# Dentro do paramentro app.run podemos passar o como parametro o "debug=True" que o mesmo reestarta a aplicação automaticamente
if __name__ == '__main__':
    app.run(debug=True)
