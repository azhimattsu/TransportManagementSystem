import copy
from tms.applicationport.order.shared.order_detail_data import OrderDetailData


class OrderDetailGetAllOutputData:
    orderinfos: list[OrderDetailData]

    def __init__(self, orderinfos: list[OrderDetailData]):
        self.orderinfos = copy.deepcopy(orderinfos)
