from tms.applicationport.container.shared.container_data_dto import ContainerDataDto
from tms.applicationport.container.put.container_put_input_data import ContainerPutInputData
from tms.domain.models.container.container_repository import ContainerRepository


class ContainersPutInteractor:
    containerRep: ContainerRepository

    def __init__(self, rep: ContainerRepository):
        self.containerRep = rep

    def update_data(self, command: ContainerPutInputData):
        entity = ContainerDataDto.to_entity(command.container)
        self.containerRep.update_data(entity)
