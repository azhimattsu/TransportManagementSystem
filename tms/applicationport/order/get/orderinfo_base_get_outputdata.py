import copy
from typing import Optional
from tms.applicationport.orderinfos.common.orderinfo_basedata import OrderInfoBaseData


class OrderInfoBaseGetOutputData:
    orderinfo: Optional[OrderInfoBaseData]

    def __init__(self, orderinfo: OrderInfoBaseData):
        self.orderinfo = copy.deepcopy(orderinfo)
