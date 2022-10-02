from tms.applicationport.orderinfos.common.orderinfodata_dto import OrderInfoDataDto
from tms.applicationport.orderinfos.post.orderinfo_post_inputdata import OrderInfoPostInputData
from tms.domain.repositories.orderinfos_repository import OrderInfosRepository


class OrderInfosPostInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def create_data(self, command: OrderInfoPostInputData):
        entity = OrderInfoDataDto.CreateEntity(command.orderinfo)
        self.orderinfosRep.create_data(entity)
