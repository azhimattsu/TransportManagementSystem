import copy
from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData


class OrderInfoGetAllOutputData:
    orderinfos: list[OrderInfoData]

    def __init__(self, orderinfos: list[OrderInfoData]):
        self.orderinfos = copy.deepcopy(orderinfos)
