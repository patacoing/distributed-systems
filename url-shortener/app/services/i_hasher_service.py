from abc import ABC, abstractmethod


class IHasherService(ABC):
    @abstractmethod
    def hash(self, id: int) -> str:
        raise NotImplementedError
