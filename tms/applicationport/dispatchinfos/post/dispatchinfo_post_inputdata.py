import copy
from tms.applicationport.dispatchinfos.common.dispatchinfodata import DispatchInfoData


class DispatchInfoPostInputData:
    dispatchinfo: DispatchInfoData

    def __init__(self, dispatchinfo: DispatchInfoData):
        self.dispatchinfo = copy.deepcopy(dispatchinfo)
