from flask import Flask, jsonify
from produtos import hamburgueres, milkshakes, refrigerantes, agua

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"mensagem": "🍔 Bem-vindo à Hamburgueria São Francisco!"})

@app.route('/cardapio/hamburgueres')
def listar_hamburgueres():
    return jsonify(hamburgueres)

@app.route('/cardapio/milkshakes')
def listar_milkshakes():
    return jsonify(milkshakes)

@app.route('/cardapio/refrigerantes')
def listar_refrigerantes():
    return jsonify(refrigerantes)

@app.route('/cardapio/agua')
def listar_agua():
    return jsonify(agua)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
