import copy
from typing import Optional
from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData


class OrderInfoGetOutputData:
    orderinfo: Optional[OrderInfoData]

    def __init__(self, orderinfo: OrderInfoData):
        self.orderinfo = copy.deepcopy(orderinfo)
