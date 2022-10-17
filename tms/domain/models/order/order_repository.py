from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional
from tms.domain.models import order


class OrderRepository(metaclass=ABCMeta):

    @abstractclassmethod
    def fetch_detail_all_data(self) -> list[order.OrderDetail]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: order.SlipCode) -> Optional[order.OrderInfo]:
        pass

    @abstractclassmethod
    def find_container_data_byorderid(self, id: order.OrderId) -> Optional[order.OrderArrangement]:
        pass

    @abstractclassmethod
    def find_detail_data_byid(self, id: order.OrderId) -> Optional[order.OrderDetail]:
        pass

    @abstractclassmethod
    def create_detail_data(self, orderdetail: order.OrderDetail):
        pass

    @abstractclassmethod
    def update_detail_data(self, orderdetail: order.OrderDetail):
        pass

    @abstractclassmethod
    def update_container_data(self, orderArrange: order.OrderArrangement):
        pass
