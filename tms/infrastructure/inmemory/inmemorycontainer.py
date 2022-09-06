from ...domain.valueobjects.containersize import ContainerSize
from ...domain.valueobjects.containerheight import ContainerHeight
from ...domain.valueobjects.tareweight import TareWeight
from ...domain.valueobjects.containertype import ContainerType
from ...domain.valueobjects.containercode import ContainerCode
from ...domain.entities.container import Container
from ...domain.repositories.containersrepository import ContainersRepository


class InMemoryContainers(ContainersRepository):

    def __init__(self):
        print("InMemoryContainers")

    def GetAllData(self) -> list[Container]:
        values = list()

        container1 = Container(ContainerCode("111111"),
                               ContainerType.TYPE_DRY,
                               TareWeight(3500),
                               ContainerHeight.HEIGHT_HIGH,
                               ContainerSize.SIZE_LONG)
        values.append(container1)
        container2 = Container(ContainerCode("222222"),
                               ContainerType.TYPE_DRY,
                               TareWeight(3500),
                               ContainerHeight.HEIGHT_NORMAL,
                               ContainerSize.SIZE_NORMAL)
        values.append(container2)
        return values
