from adapters.out.sqlite.models.categoria import Categoria

class Categoria:
    def create(self, nome):
        return Categoria.create(nome=nome)

    def get_all(self):
        return Categoria.select()

    def get_by_id(self, categoria_id):
        return Categoria.get_or_none(id=categoria_id)

    # def update(self, categoria_id, data):
    #     Categoria.update(**data).where(Categoria.id == categoria_id).execute()

    def delete(self, categoria_id):
        Categoria.delete().where(Categoria.id == categoria_id).execute()
