from typing import Optional

from ...domain.valueobjects import container
from ...domain.entities.container import ContainerEntity
from ...domain.repositories.containers_repository import ContainersRepository


class InMemoryContainers(ContainersRepository):
    containers: list[ContainerEntity] = []

    def __init__(self):
        self.containers.clear()
        container1 = ContainerEntity(container.Code("AAAA1111111"),
                                     container.Type.TYPE_DRY,
                                     container.TareWeight(3500),
                                     container.Height.HEIGHT_HIGH,
                                     container.Size.SIZE_LONG,
                                     container.Damage.DAMAGE_OK)
        self.containers.append(container1)
        container2 = ContainerEntity(container.Code("BBBB2222222"),
                                     container.Type.TYPE_DRY,
                                     container.TareWeight(3500),
                                     container.Height.HEIGHT_NORMAL,
                                     container.Size.SIZE_NORMAL,
                                     container.Damage.DAMAGE_NG)
        self.containers.append(container2)

    def fetch_all_data(self) -> list[ContainerEntity]:
        return self.containers

    def find_data_bycode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        container = next((f for f in self.containers if f.code == code), None)
        return container

    def create_data(self, container: ContainerEntity):
        self.containers.append(container)
        print(self.containers)
