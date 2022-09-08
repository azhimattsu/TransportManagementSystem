from .getall.containergetallresult import ContainerGetAllResult
from ...usecases.containers.containerdata import ContainerData
from ...domain.repositories.containersrepository import ContainersRepository


class ContainersUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def getAllData(self) -> list[ContainerData]:
        containerlist = list()
        values = self.containerRep.GetAllData()
        print(values[0].code.value)

#        for value in values:
#            containerlist.append(ContainerData(value))

        result = ContainerGetAllResult(containerlist)
        return result
