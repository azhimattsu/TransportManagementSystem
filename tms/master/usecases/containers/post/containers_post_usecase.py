from ..containermodel_dto import ContainerModelDto
from .containers_post_command import ContainersPostCommand
from ....domain.repositories.containers_repository import ContainersRepository


class ContainersPostUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def create_data(self, command: ContainersPostCommand):
        entity = ContainerModelDto.CreateEntity(command.container)
        self.containerRep.create_data(entity)
