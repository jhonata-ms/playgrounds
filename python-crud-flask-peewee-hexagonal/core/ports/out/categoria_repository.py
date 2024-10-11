from abc import ABC, abstractmethod

class CategoriaRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass
