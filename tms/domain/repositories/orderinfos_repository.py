from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from tms.domain.valueobjects import order
from tms.domain.entities.orderinfo import OrderInfoEntity


class OrderInfosRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[OrderInfoEntity]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: order.Code) -> Optional[OrderInfoEntity]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: order.id) -> Optional[OrderInfoEntity]:
        pass

    @abstractclassmethod
    def create_data(self, orderinfo: OrderInfoEntity):
        pass

    @abstractclassmethod
    def update_data(self, orderinfo: OrderInfoEntity):
        pass
