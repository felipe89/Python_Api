from flask import Flask

app = Flask(__name__)

# Dentro do parametro podemos  utilizar como metodo de requisição o "POST"  conforme exemplo
@app.route("/", methods=['POST'])
def hello():
    return u'Olá Mundo!'


if __name__ == '__main__':
    app.run(debug=True)
