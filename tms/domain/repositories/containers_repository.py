from abc import ABCMeta
from abc import abstractclassmethod

from ..valueobjects.containercode import ContainerCode
from ..entities.container import Container


class ContainersRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def GetAllData(self) -> list[Container]:
        pass

    @abstractclassmethod
    def SearchDataByCode(self, code: ContainerCode) -> Container:
        pass
