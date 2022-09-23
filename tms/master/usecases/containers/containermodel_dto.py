from tms.common.domain.valueobjects import common
from tms.master.domain.services.create_container_service import CreateContainerService
from tms.master.domain.valueobjects import container
from tms.master.domain.entities.container import ContainerEntity
from .containermodel import ContainerModel


class ContainerModelDto:

    @staticmethod
    def fromEntity(container: ContainerEntity) -> ContainerModel:
        model = ContainerModel(container.id.value,
                               container.code.value,
                               container.type,
                               container.tw.value,
                               container.height.value,
                               container.size.value,
                               container.damage.value,
                               container.createuser,
                               container.updateuser,
                               container.create_at.getStr(),
                               container.update_at.getStr())
        return model

    @staticmethod
    def toEntity(containerdata: ContainerModel) -> ContainerEntity:
        entity = ContainerEntity(container.Id(containerdata.id),
                                 container.Code(containerdata.code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage),
                                 container.MailAddress(containerdata.createuser),
                                 container.MailAddress(containerdata.updateuser),
                                 common.CDateTime(common.CreateDateTime(containerdata.create_at)),
                                 common.CDateTime(common.CreateDateTime(containerdata.update_at)))
        return entity

    @staticmethod
    def CreateEntity(containerdata: ContainerModel) -> ContainerEntity:
        entity = ContainerEntity(CreateContainerService.GetContainerId(),
                                 container.Code(containerdata.code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage),
                                 container.MailAddress(containerdata.createuser),
                                 container.MailAddress(containerdata.updateuser),
                                 common.CDateTime(common.CreateDateTime(containerdata.create_at)),
                                 common.CDateTime(common.CreateDateTime(containerdata.update_at)))
        return entity
