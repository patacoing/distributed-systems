from abc import ABC, abstractmethod


class IUniqueIdGenerator(ABC):
    @abstractmethod
    def generate_unique_id(self) -> int:
        raise NotImplementedError
