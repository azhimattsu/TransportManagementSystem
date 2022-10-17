import copy
from typing import Optional
from tms.applicationport.order.shared.order_detail_data import OrderDetailData


class OrderDetailGetOutputData:
    orderinfo: Optional[OrderDetailData]

    def __init__(self, orderinfo: OrderDetailData):
        self.orderinfo = copy.deepcopy(orderinfo)
