from tms.domain.valueobjects import common
from tms.applicationport.dispatchinfos.common.dispatchinfodata_dto import DispatchInfoDataDto
from tms.applicationport.dispatchinfos.get.dispatchinfo_get_outputdata import DispatchInfoGetOutputData
from tms.domain.repositories.dispatchinfos_repository import DispatchInfosRepository


class DispatchInfosGetInteractor:
    dispatchinfosRep: DispatchInfosRepository

    def __init__(self, rep: DispatchInfosRepository):
        self.dispatchinfosRep = rep

    def find_data_byid(self, id: str, day: str) -> DispatchInfoGetOutputData:
        dispatchinfolist = list()
        values = self.dispatchinfosRep.find_data_byid(id, common.CreateDateTime(day))
        for value in values:
            dispatchinfolist.append(DispatchInfoDataDto.fromEntity(value))

        return DispatchInfoGetOutputData(dispatchinfolist)
