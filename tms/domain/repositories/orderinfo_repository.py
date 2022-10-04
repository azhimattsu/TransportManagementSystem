from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from tms.domain.valueobjects import order
from tms.domain.entities.orderinfo_base import OrderInfoBaseEntity


class OrderInfosRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[OrderInfoBaseEntity]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: order.slicpcode) -> Optional[OrderInfoBaseEntity]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: order.id) -> Optional[OrderInfoBaseEntity]:
        pass

    @abstractclassmethod
    def create_data(self, orderinfo: OrderInfoBaseEntity):
        pass

    @abstractclassmethod
    def update_data(self, orderinfo: OrderInfoBaseEntity):
        pass
