from flask import Flask, jsonify, request
from cp.use_cases.criar_categoria import CriarCategoria

app = Flask(__name__)

@app.route('/categorias', methods=['GET'])
def get_categorias():
    return jsonify([])

@app.route('/categoria', methods=['POST'])
def create_categoria():
    data = request.json
    criar_categoria = CriarCategoria(nome=data["nome"])
    criar_categoria.executar()
    return jsonify({"retorno": "categoria criada com sucesso"}), 201
