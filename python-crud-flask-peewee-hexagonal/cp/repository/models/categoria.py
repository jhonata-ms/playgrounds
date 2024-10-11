from peewee import *

db = SqliteDatabase('financas.db')

class Categoria(Model):
    id = AutoField(column_name='ID')
    nome = CharField(column_name='NOME')

    class Meta:
        database = db
        table_name = 'CATEGORIA'

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome
        }