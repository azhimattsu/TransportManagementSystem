from ...usecases.containers.containerdata import ContainerData
from ...domain.repositories.containersrepository import ContainersRepository


class ContainersUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def getAllData(self) -> list[ContainerData]:
        containerlist = list()
        values = self.containerRep.GetAllData()
        for value in values:
            containerlist.append(ContainerData(value))
        return containerlist

#        return asyncio.run(self.containerRep.GetAllData())
