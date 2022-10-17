from tms.applicationport.container.shared.container_data_dto import ContainerDataDto
from tms.applicationport.container.post.container_post_input_data import ContainerPostInputData
from tms.domain.models.container.container_repository import ContainerRepository


class ContainersPostInteractor:
    containerRep: ContainerRepository

    def __init__(self, rep: ContainerRepository):
        self.containerRep = rep

    def create_data(self, command: ContainerPostInputData):
        entity = ContainerDataDto.CreateEntity(command.container)
        self.containerRep.create_data(entity)
