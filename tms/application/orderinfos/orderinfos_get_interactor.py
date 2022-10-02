from tms.domain.valueobjects import order
from tms.applicationport.orderinfos.common.orderinfodata_dto import OrderInfoDataDto
from tms.applicationport.orderinfos.get.orderinfo_get_outputdata import OrderInfoGetOutputData
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository


class OrderInfosGetInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def find_data_bycode(self, code: str) -> OrderInfoGetOutputData:
        orderinfodata = None
        value = self.orderinfosRep.find_data_bycode(order.SlipCode(code))
        if value is not None:
            orderinfodata = OrderInfoDataDto.from_entity(value)

        return OrderInfoGetOutputData(orderinfodata)
