from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from tms.domain.valueobjects import container
from tms.domain.entities.container import ContainerEntity


class ContainersRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[ContainerEntity]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: container.Id) -> Optional[ContainerEntity]:
        pass

    @abstractclassmethod
    def create_data(self, container: ContainerEntity):
        pass

    @abstractclassmethod
    def update_data(self, container: ContainerEntity):
        pass
