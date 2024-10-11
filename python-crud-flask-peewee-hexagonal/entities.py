
class Conta:
    def __init__(self, nome):
        self.nome = nome
    def __str__(self):
        return f'Conta(nome={self.nome})'

class Transacao:
    def __init__(self, id, data, descricao, conta, transacao):
        self.id = id
        self.data = data
        self.descricao = descricao
        self.conta = conta
        self.transacao = transacao
    def __str__(self):
        return f'Transacao(id={self.id},data={self.data},descricao={self.descricao},conta={self.conta},transacao={self.transacao})'

class Valor:
    def __init__(self, categoria, transacao, valor):
        self.categoria = categoria
        self.transacao = transacao
        self.valor = valor
    def __str__(self):
        return f'Valor(categoria={self.categoria},transacao={self.transacao},valor={self.valor})'
