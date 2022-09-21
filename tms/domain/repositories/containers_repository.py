from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from valueobjects import container
from ..entities.container import ContainerEntity


class ContainersRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[ContainerEntity]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        pass

    @abstractclassmethod
    def create_data(self, container: ContainerEntity):
        pass
