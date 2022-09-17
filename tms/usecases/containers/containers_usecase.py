from ...domain.valueobjects import container
from .containerdata_dto import ContainerModelDto
from .update.containers_update_command import ContainersUpdateCommand
from .get.containers_getresult import ContainersGetResult
from .get.containers_getallresult import ContainersGetAllResult
from ...domain.repositories.containers_repository import ContainersRepository


class ContainersUsecase:
    containerRep: ContainersRepository

    def __init__(self, rep: ContainersRepository):
        self.containerRep = rep

    def getAllData(self) -> ContainersGetAllResult:
        containerlist = list()
        values = self.containerRep.GetAllData()

        for value in values:
            containerlist.append(ContainerModelDto.fromEntity(value))

        return ContainersGetAllResult(containerlist)

    def getData(self, code: str) -> ContainersGetResult:
        value = self.containerRep.SearchDataByCode(container.Code(code))
        containerdata = ContainerModelDto.fromEntity(value)
        return ContainersGetResult(containerdata)

    def updateData(self, command: ContainersUpdateCommand):
        entity = ContainerModelDto.toEntity(command.container)
        self.containerRep.UpdateData(entity)
