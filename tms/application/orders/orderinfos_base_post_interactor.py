from tms.applicationport.orderinfos.common.orderinfo_basedata_dto import OrderInfoBaseDataDto
from tms.applicationport.orderinfos.post.orderinfo_base_post_inputdata import OrderInfoBasePostInputData
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository


class OrderInfosBasePostInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def create_data(self, command: OrderInfoBasePostInputData):
        entity = OrderInfoBaseDataDto.CreateEntity(command.orderinfo)
        self.orderinfosRep.create_data(entity)
