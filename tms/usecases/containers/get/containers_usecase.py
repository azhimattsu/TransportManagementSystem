from ....domain.valueobjects.containercode import ContainerCode
from .containers_getresult import ContainersGetResult
from .containers_getallresult import ContainersGetAllResult
from ..containerdata import ContainerData
from ....domain.repositories.containers_repository import ContainersRepository


class ContainersUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def getAllData(self) -> ContainersGetAllResult:
        containerlist = list()
        values = self.containerRep.GetAllData()

        for value in values:
            containerlist.append(ContainerData(value))

        return ContainersGetAllResult(containerlist)

    def getData(self, code: str) -> ContainersGetResult:
        value = self.containerRep.SearchDataByCode(ContainerCode(code))
        return ContainersGetResult(value)
