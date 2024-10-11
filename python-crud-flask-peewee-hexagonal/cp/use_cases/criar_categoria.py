from cp.repository.models.categoria import Categoria

class CriarCategoria:
    def __init__(self, nome):
        self.categoria = Categoria()
        self.nome = nome
    def executar(self):
        self.validar_dados()
        self.categoria.nome=self.nome
        self.categoria.save()
    def validar_dados(self):
        print("Dados do caso de uso CriarCategoria validados!")
        pass