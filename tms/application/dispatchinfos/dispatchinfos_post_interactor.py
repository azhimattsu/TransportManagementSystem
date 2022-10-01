from tms.applicationport.dispatchinfos.common.dispatchinfodata_dto import DispatchInfoDataDto
from tms.applicationport.dispatchinfos.post.dispatchinfo_post_inputdata import DispatchInfoPostInputData
from tms.domain.repositories.dispatchinfos_repository import DispatchInfosRepository


class DispatchInfosPostInteractor:
    dispatchinfosRep: DispatchInfosRepository

    def __init__(self, rep: DispatchInfosRepository):
        self.dispatchinfosRep = rep

    def create_data(self, command: DispatchInfoPostInputData):
        entity = DispatchInfoDataDto.CreateEntity(command.dispatchinfo)
        self.dispatchinfosRep.create_data(entity)
