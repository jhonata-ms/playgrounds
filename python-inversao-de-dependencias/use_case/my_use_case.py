class MyUseCase:
    def __init__(self, database):
        self.database = database
    def search_something(self):
        self.database.select()
    def insert_something(self):
        self.database.insert()
