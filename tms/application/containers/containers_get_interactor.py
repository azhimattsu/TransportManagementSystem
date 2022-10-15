from tms.domain.models import container
from tms.applicationport.container.shared.container_data_dto import ContainerDataDto
from tms.applicationport.container.get.container_get_output_data import ContainerGetOutputData
from tms.domain.models.container.container_repository import ContainerRepository


class ContainersGetInteractor:
    containerRep: ContainerRepository

    def __init__(self, rep: ContainerRepository):
        self.containerRep = rep

    def find_data_bycode(self, code: str) -> ContainerGetOutputData:
        containerdata = None
        value = self.containerRep.find_data_bycode(container.ContainerCode(code))
        if value is not None:
            containerdata = ContainerDataDto.from_entity(value)

        return ContainerGetOutputData(containerdata)
