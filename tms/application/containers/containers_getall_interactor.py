from tms.applicationport.container.shared.container_data_dto import ContainerDataDto
from tms.applicationport.container.getall.container_getall_output_data import ContainerGetAllOutputData
from tms.domain.models.container.container_repository import ContainerRepository


class ContainersGetAllInteractor:
    containerRep: ContainerRepository

    def __init__(self, rep: ContainerRepository):
        self.containerRep = rep

    def fetch_all_data(self) -> ContainerGetAllOutputData:
        containerlist = list()
        values = self.containerRep.fetch_all_data()

        for value in values:
            containerlist.append(ContainerDataDto.from_entity(value))

        return ContainerGetAllOutputData(containerlist)
