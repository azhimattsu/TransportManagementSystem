import copy
from typing import Optional
from tms.applicationport.order.shared.order_data import OrderData


class OrderGetOutputData:
    orderinfo: Optional[OrderData]

    def __init__(self, orderinfo: OrderData):
        self.orderinfo = copy.deepcopy(orderinfo)
