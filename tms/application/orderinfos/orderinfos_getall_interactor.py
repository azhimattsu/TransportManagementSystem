from tms.applicationport.orderinfos.common.orderinfodata_dto import OrderInfoDataDto
from tms.applicationport.orderinfos.getall.orderinfo_getall_outputdata import OrderInfoGetAllOutputData
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository


class OrderInfosGetAllInteractor:
    orderinfosRep: OrderInfosRepository

    def __init__(self, rep: OrderInfosRepository):
        self.orderinfosRep = rep

    def fetch_all_data(self) -> OrderInfoGetAllOutputData:
        orderinfolist = list()
        values = self.orderinfosRep.fetch_all_data()

        for value in values:
            orderinfolist.append(OrderInfoDataDto.fromEntity(value))

        return OrderInfoGetAllOutputData(orderinfolist)
