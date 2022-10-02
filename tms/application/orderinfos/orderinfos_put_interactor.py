from tms.applicationport.orderinfos.common.orderinfodata_dto import OrderInfoDataDto
from tms.applicationport.orderinfos.put.orderinfo_put_inputdata import OrderInfoPutInputData
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository


class OrderInfosPutInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def update_data(self, command: OrderInfoPutInputData):
        entity = OrderInfoDataDto.toEntity(command.orderinfo)
        self.orderinfosRep.update_data(entity)
