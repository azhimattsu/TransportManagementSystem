from tms.applicationport.containers.common.containerdata_dto import ContainerDataDto
from tms.applicationport.containers.getall.container_getall_outputdata import ContainerGetAllOutputData
from tms.domain.repositories.container_repository import ContainersRepository


class ContainersGetAllInteractor:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def fetch_all_data(self) -> ContainerGetAllOutputData:
        containerlist = list()
        values = self.containerRep.fetch_all_data()

        for value in values:
            containerlist.append(ContainerDataDto.from_entity(value))

        return ContainerGetAllOutputData(containerlist)
