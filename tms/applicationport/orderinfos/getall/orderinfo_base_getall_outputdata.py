import copy
from tms.applicationport.orderinfos.common.orderinfo_basedata import OrderInfoBaseData


class OrderInfoBaseGetAllOutputData:
    orderinfos: list[OrderInfoBaseData]

    def __init__(self, orderinfos: list[OrderInfoBaseData]):
        self.orderinfos = copy.deepcopy(orderinfos)
