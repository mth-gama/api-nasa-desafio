from flask import Flask ,jsonify ,render_template


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/confidencial')
def response_estaplanetar():
    with open('x.txt','r') as arquivoX:
        confidencial = arquivoX.read()

    with open('loc.txt','r') as arquivoloc:
        loc = arquivoloc.read()
    
    with open('exploracao.txt','r') as exp:
        expExpedicao = exp.read()

    dados ={'confidencial':confidencial,'localizacao':loc,'expedicao':expExpedicao}

    return jsonify(dados)


if __name__ == '__main__':
    app.run()