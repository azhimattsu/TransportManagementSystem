from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional
from tms.domain.entities.orderinfo import OrderInfoEntity
from tms.domain.entities.orderinfo_container import OrderInfoContainerEntity

from tms.domain.valueobjects import order
from tms.domain.entities.orderinfo_base import OrderInfoBaseEntity


class OrderInfosRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[OrderInfoBaseEntity]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: order.SlipCode) -> Optional[OrderInfoBaseEntity]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: order.Id) -> Optional[OrderInfoBaseEntity]:
        pass

    @abstractclassmethod
    def create_data(self, orderinfo: OrderInfoBaseEntity):
        pass

    @abstractclassmethod
    def update_data(self, orderinfo: OrderInfoBaseEntity):
        pass

    @abstractclassmethod
    def fetch_container_data_byorderid(self, id: order.Id) -> list[OrderInfoContainerEntity]:
        pass

    @abstractclassmethod
    def find_fulldata_byid(self, id: order.id) -> Optional[OrderInfoEntity]:
        pass
