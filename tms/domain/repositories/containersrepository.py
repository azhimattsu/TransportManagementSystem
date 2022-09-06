from abc import ABCMeta
from abc import abstractclassmethod
from ..entities.container import Container


class ContainersRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def GetAllData(self) -> list[Container]:
        pass
