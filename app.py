from flask import Flask ,jsonify ,render_template


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')


def dados_capacete(arquivo):
    with open(f'{arquivo}','r') as metadados:
        return metadados.read()

def dados_traje(arquivo):
    with open(f'{arquivo}','r') as metadados:
        return metadados.read()
    
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

@app.route('/astronauta')
def response_infoastronauta():
    
    dr_man_capacete = dados_capacete('astronautas/capacete/dr_man.txt')
    dr_man_traje = dados_traje('astronautas/roupa/dr_man.txt')
    dra_brand_capacete = dados_capacete('astronautas/capacete/dra_brand.txt')
    dra_brand_traje = dados_traje('astronautas/roupa/dra_brand.txt')

    dados = {'dr.man_capacete':dr_man_capacete,'dra.brand_capacete':dra_brand_capacete,'dr.man_traje':dr_man_traje,'dra.man_traje':dra_brand_traje}
    return jsonify(dados)

if __name__ == '__main__':
    app.run()