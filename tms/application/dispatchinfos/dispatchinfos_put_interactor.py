from tms.applicationport.dispatchinfos.common.dispatchinfodata_dto import DispatchInfoDataDto
from tms.applicationport.dispatchinfos.put.dispatchinfo_put_inputdata import DispatchInfoPutInputData
from tms.domain.repositories.dispatchinfo_repository import DispatchInfosRepository


class DispatchInfosPutInteractor:
    dispatchinfosRep: DispatchInfosRepository

    def __init__(self, rep: DispatchInfosRepository):
        self.dispatchinfosRep = rep

    def update_data(self, command: DispatchInfoPutInputData):
        entity = DispatchInfoDataDto.toEntity(command.dispatchinfo)
        self.dispatchinfosRep.update_data(entity)
