from tms.domain.models import order
from tms.applicationport.order.shared.order_detail_data_dto import OrderDetailDataDto
from tms.applicationport.order.get.order_detail_get_output_data import OrderDetailGetOutputData
from tms.domain.models.order import OrderRepository


class OrderDetailGetInteractor:
    orderinfosRep: OrderRepository

    def __init__(self, rep: OrderRepository):
        self.orderinfosRep = rep

    def find_data_byid(self, id: str) -> OrderDetailGetOutputData:
        orderinfodata = None
        value = self.orderinfosRep.find_detail_data_byid(order.OrderId(id))
        if value is not None:
            orderinfodata = OrderDetailDataDto.from_entity(value)

        return OrderDetailGetOutputData(orderinfodata)
