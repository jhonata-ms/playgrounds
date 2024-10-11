from abc import ABC, abstractmethod
from core.port.out.categoria_repository import CategoriaRepository

class Database(CategoriaRepository, ABC):
    pass
