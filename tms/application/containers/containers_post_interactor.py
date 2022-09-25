from tms.applicationport.containers.common.containerdata_dto import ContainerDataDto
from tms.applicationport.containers.post.container_post_inputdata import ContainerPostInputData
from tms.domain.repositories.containers_repository import ContainersRepository


class ContainersPostInteractor:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def create_data(self, command: ContainerPostInputData):
        entity = ContainerDataDto.CreateEntity(command.container)
        self.containerRep.create_data(entity)
