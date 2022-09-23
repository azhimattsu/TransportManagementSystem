from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from tms.master.domain.valueobjects import container
from tms.master.domain.entities.container import ContainerEntity


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
