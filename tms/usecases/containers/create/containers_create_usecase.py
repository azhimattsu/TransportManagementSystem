from ..containermodel_dto import ContainerModelDto
from .containers_create_command import ContainersCreateCommand
from ....domain.repositories.containers_repository import ContainersRepository


class ContainersCreateUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def create_data(self, command: ContainersCreateCommand):
        entity = ContainerModelDto.toEntity(command.container)
        self.containerRep.create_data(entity)
