from tms.domain.valueobjects import container
from tms.applicationport.containers.common.containerdata_dto import ContainerDataDto
from tms.applicationport.containers.get.container_get_outputdata import ContainerGetOutputData
from tms.domain.repositories.containers_repository import ContainersRepository


class ContainersGetInteractor:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def find_data_bycode(self, code: str) -> ContainerGetOutputData:
        value = self.containerRep.find_data_bycode(container.Code(code))
        if value is not None:
            containerdata = ContainerDataDto.fromEntity(value)

        return ContainerGetOutputData(containerdata)
