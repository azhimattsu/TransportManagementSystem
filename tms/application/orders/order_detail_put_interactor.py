from tms.applicationport.order.shared.order_detail_data_dto import OrderDetailDataDto
from tms.applicationport.order.put.order_detail_put_input_data import OrderDetailPutInputData
from tms.domain.models.order.order_repository import OrderRepository


class OrderDetailPutInteractor:
    orderinfosRep: OrderRepository

    def __init__(self, rep: OrderRepository):
        self.orderinfosRep = rep

    def update_data(self, command: OrderDetailPutInputData):
        entity = OrderDetailDataDto.to_entity(command.orderinfo)
        self.orderinfosRep.update_detail_data(entity)
