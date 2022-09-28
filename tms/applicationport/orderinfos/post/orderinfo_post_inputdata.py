import copy
from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData


class OrderInfoPostInputData:
    orderinfo: OrderInfoData

    def __init__(self, orderinfo: OrderInfoData):
        self.orderinfo = copy.deepcopy(orderinfo)
