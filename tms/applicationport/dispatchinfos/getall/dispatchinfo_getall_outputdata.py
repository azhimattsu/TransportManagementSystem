import copy
from tms.applicationport.dispatchinfos.common.dispatchinfodata import DispatchInfoData


class DispatchInfoGetAllOutputData:
    dispatchinfos: list[DispatchInfoData]

    def __init__(self, dispatchinfos: list[DispatchInfoData]):
        self.dispatchinfos = copy.deepcopy(dispatchinfos)
