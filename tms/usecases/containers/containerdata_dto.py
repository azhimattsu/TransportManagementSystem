from ...domain.valueobjects.containercode import ContainerCode
from ...domain.valueobjects.containerdamage import ContainerDamage
from ...domain.valueobjects.containerheight import ContainerHeight
from ...domain.valueobjects.containersize import ContainerSize
from ...domain.valueobjects.containertype import ContainerType
from ...domain.valueobjects.tareweight import TareWeight
from ...domain.entities.container import Container
from .containerdata import ContainerData


class ContainerDataDto:

    @staticmethod
    def fromEntity(container: Container) -> ContainerData:
        containerdata = ContainerData(container.code.value,
                                      container.type.value,
                                      container.tw.value,
                                      container.height.value,
                                      container.size.value,
                                      container.damage.value)
        return containerdata

    @staticmethod
    def toEntity(containerdata: ContainerData) -> Container:
        container = Container(ContainerCode(containerdata.code),
                              ContainerType(containerdata.type),
                              TareWeight(containerdata.tw),
                              ContainerHeight(containerdata.height),
                              ContainerSize(containerdata.size),
                              ContainerDamage(containerdata.damage))
        return container
