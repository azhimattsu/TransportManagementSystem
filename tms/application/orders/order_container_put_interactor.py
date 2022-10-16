from tms.applicationport.order.shared.order_container_data_dto import OrderContainerDataDto
from tms.applicationport.order.put.order_container_put_input_data import OrderContainerPutInputData
from tms.domain.models.order.order_repository import OrderRepository
from tms.domain.models.order.order_arrangement import OrderArrangement
from tms.domain.models import order


class OrderContainerPutInteractor:
    orderinfosRep: OrderRepository

    def __init__(self, rep: OrderRepository):
        self.orderinfosRep = rep

    def update_data(self, command: OrderContainerPutInputData):
        items = OrderContainerDataDto.to_entity(command.orderinfo)
        entity = OrderArrangement(order.OrderId(command.get_order_id()), items)
        self.orderinfosRep.update_container_data(entity)
