import copy
from tms.applicationport.order.shared.order_detail_data import OrderDetailData


class OrderDetailPutInputData:
    orderinfo: OrderDetailData

    def __init__(self, orderinfo: OrderDetailData):
        self.orderinfo = copy.deepcopy(orderinfo)
