from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from tms.domain.models import container


class ContainerRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[container.ContainerInfo]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: container.ContainerCode) -> Optional[container.ContainerInfo]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: container.ContainerId) -> Optional[container.ContainerInfo]:
        pass

    @abstractclassmethod
    def create_data(self, container: container.ContainerInfo):
        pass

    @abstractclassmethod
    def update_data(self, container: container.ContainerInfo):
        pass
