from tms.applicationport.order.shared.order_detail_data_dto import OrderDetailDataDto
from tms.applicationport.order.post.order_detail_post_input_data import OrderDetailPostInputData
from tms.domain.models.order.order_repository import OrderRepository


class OrderDetailPostInteractor:
    orderinfosRep: OrderRepository

    def __init__(self, rep: OrderRepository):
        self.orderinfosRep = rep

    def create_data(self, command: OrderDetailPostInputData):
        entity = OrderDetailDataDto.CreateEntity(command.orderinfo)
        self.orderinfosRep.create_detail_data(entity)
