import copy
from typing import Optional
from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData


class OrderInfoGetOutputData:
    container: Optional[OrderInfoData]

    def __init__(self, orderinfo: OrderInfoData):
        self.container = copy.deepcopy(orderinfo)
