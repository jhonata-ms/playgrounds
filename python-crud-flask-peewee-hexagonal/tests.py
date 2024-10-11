from adapters.out.sqlite.models.categoria import Categoria
print(Categoria.select().get())

# from datetime import datetime
# from domain.categoria import Categoria
# from domain.transacao import Transacao
# from domain.conta import Conta
# from domain.valor import Valor

# categoria = Categoria(None, 'Videogames')
# conta = Conta(None, 'NuBank')
# transacao = Transacao(None, datetime(2024, 3, 11).date(), 'Super Ultra Mega Video Game', conta, None)
# valor = Valor(None, categoria, transacao, 3700.0)

# print(valor)



# from infra.persistence.sqlite.categoria import Categoria

# # Examplo de delete all
# Categoria.delete().execute()

# categoria = Categoria(nome='Água')
# categoria.save()

# # Exemplo de read all
# for categoria in Categoria.select():
#     print(categoria.nome)

# # Exemplo de read e update
# categoria = Categoria.select().where(Categoria.nome == 'Luz').get()
# categoria.nome = 'Eletricidade'
# categoria.save()

# for categoria in Categoria.select():
#     print(categoria.nome)

# # Exemplo de delete
# categoria = Categoria.select().where(Categoria.nome == 'Eletricidade').get()
# categoria.delete_instance()

# for categoria in Categoria.select():
#     print(categoria.nome)

# # Exemplo de read by id
# categoria = Categoria.get_by_id(33)
# print(categoria.nome)





# file: adapters.in.rest

# @app.route('/categoria/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = user_service.get_user_by_id(user_id)
#     return jsonify(user.__dict__['_data']) if user else ('', 404)

# @app.route('/categoria/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     data = request.json
#     user_service.update_user(user_id, data)
#     return '', 204

# @app.route('/categoria/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user_service.delete_user(user_id)
#     return '', 204


# file: ?

# from adapters.out.sqlite.adapter_sqlite import CategoriaRepository

# # Aqui deve ficar a regra de negócio! Não deveria mover este arquivo para core?

# class CategoriaService:
#     def __init__(self):
#         self.categoria_repository = CategoriaRepository()

#     def create_categoria(self, nome):
#         return self.categoria_repository.create(nome)

#     def get_all_categorias(self):
#         return self.categoria_repository.get_all()

#     def get_categoria_by_id(self, categoria_id):
#         return self.categoria_repository.get_by_id(categoria_id)

#     # def update_categoria(self, categoria_id, data):
#     #     self.categoria_repository.update(categoria_id, data)

#     def delete_categoria(self, categoria_id):
#         self.categoria_repository.delete(categoria_id)




# file: port.out.categoria_repository.py

    # @abstractmethod
    # def create(self, nome):
    #     pass

    # @abstractmethod
    # def get_by_id(self, categoria_id):
    #     pass

    # @abstractmethod
    # def update(self, categoria_id, nome):
    #     pass

    # @abstractmethod
    # def delete(self, categoria_id):
    #     pass

