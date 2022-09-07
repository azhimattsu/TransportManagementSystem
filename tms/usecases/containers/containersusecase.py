
from ...domain.entities.container import Container
from ...domain.repositories.containersrepository import ContainersRepository


class ContainersUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def getAllData(self) -> list[Container]:
        return self.containerRep.GetAllData()

#        return asyncio.run(self.containerRep.GetAllData())
