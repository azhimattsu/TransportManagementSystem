from tms.applicationport.order.shared.order_data_dto import OrderDataDto
from tms.applicationport.order.get.order_get_output_data import OrderGetOutputData
from tms.domain.models import order
from tms.domain.models.order.order_repository import OrderRepository


class OrderGetInteractor:
    orderinfosRep: OrderRepository

    def __init__(self, rep: OrderRepository):
        self.orderinfosRep = rep

    def find_data_bycode(self, code: str) -> OrderGetOutputData:
        orderinfodata = None
        value = self.orderinfosRep.find_data_bycode(order.SlipCode(code))
        if value is not None:
            orderinfodata = OrderDataDto.from_entity(value)

        return OrderGetOutputData(orderinfodata)
