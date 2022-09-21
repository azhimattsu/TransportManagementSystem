from tms.master.domain.services.create_container_service import CreateContainerService
from ...domain.valueobjects import container
from ...domain.entities.container import ContainerEntity
from .containermodel import ContainerModel


class ContainerModelDto:

    @staticmethod
    def fromEntity(container: ContainerEntity) -> ContainerModel:
        model = ContainerModel(container.id.value,
                               container.code.value,
                               container.type.value,
                               container.tw.value,
                               container.height.value,
                               container.size.value,
                               container.damage.value)
        return model

    @staticmethod
    def toEntity(containerdata: ContainerModel) -> ContainerEntity:
        entity = ContainerEntity(container.Id(containerdata.id),
                                 container.Code(containerdata.code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage))
        return entity

    @staticmethod
    def CreateEntity(containerdata: ContainerModel) -> ContainerEntity:
        entity = ContainerEntity(CreateContainerService.GetContainerId(),
                                 container.Code(containerdata.code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage))
        return entity
