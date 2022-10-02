from tms.applicationport.containers.common.containerdata_dto import ContainerDataDto
from tms.applicationport.containers.put.container_put_inputdata import ContainerPutInputData
from tms.domain.repositories.container_repository import ContainersRepository


class ContainersPutInteractor:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def update_data(self, command: ContainerPutInputData):
        entity = ContainerDataDto.toEntity(command.container)
        self.containerRep.update_data(entity)
