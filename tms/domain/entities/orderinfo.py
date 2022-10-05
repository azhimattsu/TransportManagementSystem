import copy
from dataclasses import dataclass
from tms.domain.entities.orderinfo_base import OrderInfoBaseEntity
from tms.domain.entities.orderinfo_container import OrderInfoContainerEntity


@dataclass(init=False, eq=True)
class OrderInfoEntity(OrderInfoBaseEntity):
    orderinfo: OrderInfoBaseEntity
    containers: list[OrderInfoContainerEntity]

    def __init__(self,
                 orderinfo: OrderInfoBaseEntity,
                 containers: list[OrderInfoContainerEntity]):

        self.orderinfo = copy.deepcopy(orderinfo)
        self.containers = copy.deepcopy(containers)
