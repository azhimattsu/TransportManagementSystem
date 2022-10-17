from tms.domain.models import container
from tms.domain.models import shared
from tms.domain.services.create_container_service import CreateContainerService
from .container_data import ContainerData


class ContainerDataDto:

    @staticmethod
    def from_entity(container: container.ContainerInfo) -> ContainerData:
        model = ContainerData(container.container_id.value,
                              container.container_code.value,
                              container.type,
                              container.tw.value,
                              container.height.value,
                              container.size.value,
                              container.damage.value,
                              container.update_info.create_user.value,
                              container.update_info.update_user.value,
                              container.update_info.create_at.getStr(),
                              container.update_info.update_at.getStr())
        return model

    @staticmethod
    def to_entity(containerdata: ContainerData) -> container.ContainerInfo:
        entity = container.ContainerInfo(container.ContainerId(containerdata.container_id),
                                         container.ContainerCode(containerdata.container_code),
                                         container.Type(containerdata.type),
                                         container.TareWeight(containerdata.tw),
                                         container.Height(containerdata.height),
                                         container.Size(containerdata.size),
                                         container.Damage(containerdata.damage),
                                         shared.UpdateInfo(shared.MailAddress(containerdata.create_user),
                                         shared.MailAddress(containerdata.update_user),
                                         shared.CreateDateTime(containerdata.create_at),
                                         shared.CreateDateTime(containerdata.update_at)))
        return entity

    @staticmethod
    def CreateEntity(containerdata: ContainerData) -> container.ContainerInfo:
        entity = container.ContainerInfo(CreateContainerService.get_containerid(),
                                         container.ContainerCode(containerdata.container_code),
                                         container.Type(containerdata.type),
                                         container.TareWeight(containerdata.tw),
                                         container.Height(containerdata.height),
                                         container.Size(containerdata.size),
                                         container.Damage(containerdata.damage),
                                         shared.UpdateInfo(shared.MailAddress(containerdata.create_user),
                                         shared.MailAddress(containerdata.update_user),
                                         shared.CreateDateTime(containerdata.create_at),
                                         shared.CreateDateTime(containerdata.update_at)))
        return entity
