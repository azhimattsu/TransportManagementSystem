from typing import Optional

from ...domain.valueobjects.containerdamage import ContainerDamage
from ...domain.valueobjects.containersize import ContainerSize
from ...domain.valueobjects.containerheight import ContainerHeight
from ...domain.valueobjects.tareweight import TareWeight
from ...domain.valueobjects.containertype import ContainerType
from ...domain.valueobjects.containercode import ContainerCode
from ...domain.entities.container import Container
from ...domain.repositories.containers_repository import ContainersRepository


class InMemoryContainers(ContainersRepository):
    containers: list[Container] = []

    def __init__(self):
        self.containers.clear()
        container1 = Container(ContainerCode("AAAA-111111"),
                               ContainerType.TYPE_DRY,
                               TareWeight(3500),
                               ContainerHeight.HEIGHT_HIGH,
                               ContainerSize.SIZE_LONG,
                               ContainerDamage.DAMAGE_OK)
        self.containers.append(container1)
        container2 = Container(ContainerCode("BBBB-222222"),
                               ContainerType.TYPE_DRY,
                               TareWeight(3500),
                               ContainerHeight.HEIGHT_NORMAL,
                               ContainerSize.SIZE_NORMAL,
                               ContainerDamage.DAMAGE_NG)
        self.containers.append(container2)

    def GetAllData(self) -> list[Container]:
        return self.containers

    def SearchDataByCode(self, code: ContainerCode) -> Optional[Container]:
        container = next((f for f in self.containers if f.code == code), None)
        return container
