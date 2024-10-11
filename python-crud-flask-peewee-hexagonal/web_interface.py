from abc import ABC, abstractmethod
from core.port.out.categoria_repository import CategoriaRepository

class Web(CategoriaRepository, ABC):
    pass
