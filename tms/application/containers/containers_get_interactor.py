from tms.domain.valueobjects import container
from tms.applicationport.containers.common.containerdata_dto import ContainerDataDto
from tms.applicationport.containers.get.container_get_outputdata import ContainerGetOutputData
from tms.domain.repositories.container_repository import ContainersRepository


class ContainersGetInteractor:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def find_data_bycode(self, code: str) -> ContainerGetOutputData:
        containerdata = None
        value = self.containerRep.find_data_bycode(container.Code(code))
        if value is not None:
            containerdata = ContainerDataDto.from_entity(value)

        return ContainerGetOutputData(containerdata)
