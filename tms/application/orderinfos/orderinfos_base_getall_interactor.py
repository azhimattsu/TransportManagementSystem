from tms.applicationport.orderinfos.common.orderinfo_basedata_dto import OrderInfoBaseDataDto
from tms.applicationport.orderinfos.getall.orderinfo_base_getall_outputdata import OrderInfoBaseGetAllOutputData
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository


class OrderInfosBaseGetAllInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def fetch_all_data(self) -> OrderInfoBaseGetAllOutputData:
        orderinfolist = list()
        values = self.orderinfosRep.fetch_all_data()

        for value in values:
            orderinfolist.append(OrderInfoBaseDataDto.from_entity(value))

        return OrderInfoBaseGetAllOutputData(orderinfolist)
