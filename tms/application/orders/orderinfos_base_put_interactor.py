from tms.applicationport.orderinfos.common.orderinfo_basedata_dto import OrderInfoBaseDataDto
from tms.applicationport.orderinfos.put.orderinfo_base_put_inputdata import OrderInfoBasePutInputData
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository


class OrderInfosBasePutInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def update_data(self, command: OrderInfoBasePutInputData):
        entity = OrderInfoBaseDataDto.to_entity(command.orderinfo)
        self.orderinfosRep.update_data(entity)
