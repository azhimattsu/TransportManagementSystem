from tms.domain.valueobjects import order
from tms.applicationport.orderinfos.common.orderinfo_basedata_dto import OrderInfoBaseDataDto
from tms.applicationport.orderinfos.get.orderinfo_base_get_outputdata import OrderInfoBaseGetOutputData
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository


class OrderInfosBaseGetInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def find_data_bycode(self, code: str) -> OrderInfoBaseGetOutputData:
        orderinfodata = None
        value = self.orderinfosRep.find_data_bycode(order.SlipCode(code))
        if value is not None:
            orderinfodata = OrderInfoBaseDataDto.from_entity(value)

        return OrderInfoBaseGetOutputData(orderinfodata)
