from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from ..valueobjects import container
from ..entities.container import ContainerEntity


class ContainersRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def GetAllData(self) -> list[ContainerEntity]:
        pass

    @abstractclassmethod
    def SearchDataByCode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        pass

    @abstractclassmethod
    def UpdateData(self, container: ContainerEntity):
        pass
