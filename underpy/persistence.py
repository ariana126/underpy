from abc import ABC, abstractmethod

from underpy import JSON


class Persistable(ABC):
    @abstractmethod
    def to_json(self) -> JSON:
        pass

    @staticmethod
    @abstractmethod
    def from_json(cls, dat: JSON) -> 'Persistable':
        pass

class Repository(ABC):
    @abstractmethod
    def save(self, persistable: Persistable) -> None:
        pass

    def find(self, id_) -> Persistable|None:
        pass

    def get(self, id_) -> Persistable:
        persistable = self.find(id_)
        if persistable is None:
            raise RuntimeError(f"Entity not found with id: {id_}")
        return persistable