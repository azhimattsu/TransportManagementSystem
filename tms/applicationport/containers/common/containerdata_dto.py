from tms.domain.valueobjects import common
from tms.domain.services.create_container_service import CreateContainerService
from tms.domain.valueobjects import container
from tms.domain.entities.container import ContainerEntity
from .containerdata import ContainerData


class ContainerDataDto:

    @staticmethod
    def from_entity(container: ContainerEntity) -> ContainerData:
        model = ContainerData(container.container_id.value,
                              container.container_code.value,
                              container.type,
                              container.tw.value,
                              container.height.value,
                              container.size.value,
                              container.damage.value,
                              container.create_user.value,
                              container.update_user.value,
                              container.create_at.getStr(),
                              container.update_at.getStr())
        return model

    @staticmethod
    def to_entity(containerdata: ContainerData) -> ContainerEntity:
        entity = ContainerEntity(container.Id(containerdata.container_id),
                                 container.Code(containerdata.container_code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage),
                                 common.MailAddress(containerdata.create_user),
                                 common.MailAddress(containerdata.update_user),
                                 common.CreateDateTime(containerdata.create_at),
                                 common.CreateDateTime(containerdata.update_at))
        return entity

    @staticmethod
    def CreateEntity(containerdata: ContainerData) -> ContainerEntity:
        entity = ContainerEntity(CreateContainerService.get_containerid(),
                                 container.Code(containerdata.container_code),
                                 container.Type(containerdata.type),
                                 container.TareWeight(containerdata.tw),
                                 container.Height(containerdata.height),
                                 container.Size(containerdata.size),
                                 container.Damage(containerdata.damage),
                                 common.MailAddress(containerdata.create_user),
                                 common.MailAddress(containerdata.update_user),
                                 common.CreateDateTime(containerdata.create_at),
                                 common.CreateDateTime(containerdata.update_at))
        return entity
