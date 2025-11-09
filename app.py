from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contatos')
def contatos():
    lista_contatos = [
        {"nome": "Contato 1", "email": "contato1@ifrn.edu.br"},
        {"nome": "Contato 2", "email": "contato2@ifrn.edu.br"},
        {"nome": "Contato 3", "email": "contato3@ifrn.edu.br"},
        {"nome": "Contato 4", "email": "contato4@ifrn.edu.br"},
        {"nome": "Contato 5", "email": "contato5@ifrn.edu.br"},
        {"nome": "Contato 6", "email": "contato6@ifrn.edu.br"},
    ]
    return render_template('contatos.html', contatos=lista_contatos)


if __name__ == '__main__':
    app.run(debug=True)
