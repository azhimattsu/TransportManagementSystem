from dataclasses import dataclass

from tms.domain.models import order


@dataclass(init=False, eq=True)
class OrderInfo:
    order_id: order.OrderId
    slip_code: order.SlipCode
    detail_info: order.OrderDetail
    arrangement_info: order.OrderArrangement

    def __init__(self,
                 order_id: order.OrderId,
                 slip_code: order.SlipCode,
                 detail_info: order.OrderDetail,
                 arrangement_info: order.OrderArrangement):
        self.order_id = order_id
        self.slip_code = slip_code
        self.detail_info = detail_info
        self.arrangement_info = arrangement_info
