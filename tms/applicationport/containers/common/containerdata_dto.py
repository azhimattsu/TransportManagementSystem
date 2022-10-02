from tms.domain.valueobjects import common
from tms.domain.services.create_container_service import CreateContainerService
from tms.domain.valueobjects import container
from tms.domain.entities.container import ContainerEntity
from .containerdata import ContainerData


class ContainerDataDto:

    @staticmethod
    def fromEntity(container: ContainerEntity) -> ContainerData:
        model = ContainerData(container.id.value,
                              container.code.value,
                              container.type,
                              container.tw.value,
                              container.height.value,
                              container.size.value,
                              container.damage.value,
                              container.createuser.value,
                              container.updateuser.value,
                              container.create_at.getStr(),
                              container.update_at.getStr())
        return model

    @staticmethod
    def toEntity(containerdata: ContainerData) -> ContainerEntity:
        entity = ContainerEntity(container.Id(containerdata.id),
                                 container.Code(containerdata.code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage),
                                 common.MailAddress(containerdata.createuser),
                                 common.MailAddress(containerdata.updateuser),
                                 common.CreateDateTime(containerdata.create_at),
                                 common.CreateDateTime(containerdata.update_at))
        return entity

    @staticmethod
    def CreateEntity(containerdata: ContainerData) -> ContainerEntity:
        entity = ContainerEntity(CreateContainerService.GetContainerId(),
                                 container.Code(containerdata.code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage),
                                 common.MailAddress(containerdata.createuser),
                                 common.MailAddress(containerdata.updateuser),
                                 common.CreateDateTime(containerdata.create_at),
                                 common.CreateDateTime(containerdata.update_at))
        return entity
