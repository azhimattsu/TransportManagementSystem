from ...domain.valueobjects.containercode import ContainerCode
from .containerdata_dto import ContainerDataDto
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
            containerlist.append(ContainerDataDto.fromEntity(value))

        return ContainersGetAllResult(containerlist)

    def getData(self, code: str) -> ContainersGetResult:
        value = self.containerRep.SearchDataByCode(ContainerCode(code))
        container = ContainerDataDto.fromEntity(value)
        return ContainersGetResult(container)

    def updateData(self, command: ContainersUpdateCommand):
        entity = ContainerDataDto.toEntity(command.container)
        self.containerRep.UpdateData(entity)
