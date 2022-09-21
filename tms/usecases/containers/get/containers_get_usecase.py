from ....domain.valueobjects import container
from ..containermodel_dto import ContainerModelDto
from .containers_getresult import ContainersGetResult
from .containers_getallresult import ContainersGetAllResult
from ....domain.repositories.containers_repository import ContainersRepository


class ContainersGetUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def fetch_all_data(self) -> ContainersGetAllResult:
        containerlist = list()
        values = self.containerRep.fetch_all_data()

        for value in values:
            containerlist.append(ContainerModelDto.fromEntity(value))

        return ContainersGetAllResult(containerlist)

    def find_data_bycode(self, code: str) -> ContainersGetResult:
        value = self.containerRep.find_data_bycode(container.Code(code))
        containerdata = ContainerModelDto.fromEntity(value)
        return ContainersGetResult(containerdata)
