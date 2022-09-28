import copy
from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData


class OrderInfoPutInputData:
    orderinfo: OrderInfoData

    def __init__(self, orderinfo: OrderInfoData):
        self.orderinfo = copy.deepcopy(orderinfo)
