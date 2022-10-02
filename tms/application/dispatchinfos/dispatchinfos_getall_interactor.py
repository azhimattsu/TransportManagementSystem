from tms.applicationport.dispatchinfos.common.dispatchinfodata_dto import DispatchInfoDataDto
from tms.applicationport.dispatchinfos.getall.dispatchinfo_getall_outputdata import DispatchInfoGetAllOutputData
from tms.domain.repositories.dispatchinfo_repository import DispatchInfosRepository


class DispatchInfosGetAllInteractor:
    dispatchinfosRep: DispatchInfosRepository

    def __init__(self, rep: DispatchInfosRepository):
        self.dispatchinfosRep = rep

    def fetch_all_data(self) -> DispatchInfoGetAllOutputData:
        dispatchinfolist = list()
        values = self.dispatchinfosRep.fetch_all_data()

        for value in values:
            dispatchinfolist.append(DispatchInfoDataDto.fromEntity(value))

        return DispatchInfoGetAllOutputData(dispatchinfolist)
