import copy
from tms.applicationport.orderinfos.common.orderinfo_basedata import OrderInfoBaseData


class OrderInfoBasePutInputData:
    orderinfo: OrderInfoBaseData

    def __init__(self, orderinfo: OrderInfoBaseData):
        self.orderinfo = copy.deepcopy(orderinfo)
