from tms.applicationport.order.shared.order_detail_data_dto import OrderDetailDataDto
from tms.applicationport.order.getall.order_detail_getall_output_data import OrderDetailGetAllOutputData
from tms.domain.models.order import OrderRepository


class OrderDetailGetAllInteractor:
    orderinfosRep: OrderRepository

    def __init__(self, rep: OrderRepository):
        self.orderinfosRep = rep

    def fetch_all_data(self) -> OrderDetailGetAllOutputData:
        orderinfolist = list()
        values = self.orderinfosRep.fetch_detail_all_data()

        for value in values:
            orderinfolist.append(OrderDetailDataDto.from_entity(value))

        return OrderDetailGetAllOutputData(orderinfolist)
