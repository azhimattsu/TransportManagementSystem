from typing import Optional

from tms.domain.valueobjects import container
from tms.domain.entities.container import ContainerEntity
from tms.domain.repositories.containers_repository import ContainersRepository
from tms.domain.valueobjects import common


class InMemoryContainers(ContainersRepository):
    containers: list[ContainerEntity] = []

    def __init__(self):
        self.containers.clear()
        container1 = ContainerEntity(container.Id("a8d0a2d7-76c5-ad57-dd0b-ee566152441e"),
                                     container.Code("AAAA1111111"),
                                     container.Type.TYPE_DRY,
                                     container.TareWeight(3500),
                                     container.Height.HEIGHT_HIGH,
                                     container.Size.SIZE_LONG,
                                     container.Damage.DAMAGE_OK,
                                     "test001@test.com",
                                     "test001@test.com",
                                     common.CreateDateTime("2017-05-23 12:47:23"),
                                     common.CreateDateTime("2017-05-23 12:47:23"))
        self.containers.append(container1)
        container2 = ContainerEntity(container.Id("1d02a8b7-a6c4-fe2d-635a-a6829bbef6c7"),
                                     container.Code("BBBB2222222"),
                                     container.Type.TYPE_DRY,
                                     container.TareWeight(3500),
                                     container.Height.HEIGHT_NORMAL,
                                     container.Size.SIZE_NORMAL,
                                     container.Damage.DAMAGE_NG,
                                     "test001@test.com",
                                     "test001@test.com",
                                     common.CreateDateTime("2017-05-23 12:47:23"),
                                     common.CreateDateTime("2017-05-23 12:47:23"))
        self.containers.append(container2)

    def fetch_all_data(self) -> list[ContainerEntity]:
        return self.containers

    def find_data_bycode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        container = next((f for f in self.containers if f.code == code), None)
        return container

    def find_data_byid(self, id: container.id) -> Optional[ContainerEntity]:
        container = next((f for f in self.containers if f.id == id), None)
        return container

    def create_data(self, container: ContainerEntity):
        self.containers.append(container)
        print(self.containers)

    def update_data(self, container: ContainerEntity):
        pass
