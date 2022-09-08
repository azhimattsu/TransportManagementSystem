from .getall.containergetallresult import ContainerGetAllResult
from ...usecases.containers.containerdata import ContainerData
from ...domain.repositories.containersrepository import ContainersRepository


class ContainersUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def getAllData(self) -> ContainerGetAllResult:
        containerlist = list()
        values = self.containerRep.GetAllData()

        for value in values:
            containerlist.append(ContainerData(value))

        result = ContainerGetAllResult(containerlist)
        return result
