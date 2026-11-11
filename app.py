from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
@app.route('/quemsomos.html')
def quemsomos():
    return render_template('quemsomos.html')

@app.route('/comocuidar')
@app.route('/comocuidar.html')
def comocuidar():
    return render_template('comocuidar.html')

@app.route('/agendamento')
@app.route('/agendamento.html')
def agendamento():
    return render_template('agendamento.html')

if __name__ == '__main__':
    # Configurado para aceitar conexoes externas na porta 5000 (requisito Etapa 6)
    app.run(host='0.0.0.0', port=5000, debug=False)
