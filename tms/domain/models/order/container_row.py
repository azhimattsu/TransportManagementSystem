from dataclasses import dataclass

from tms.domain.models import shared
from tms.domain.models import order
from tms.domain.models import container


@dataclass(init=False, eq=True)
class ContainerRow():
    order_id: order.OrderId
    sort_id: int
    container_id: container.ContainerId
    freight: int
    surcharge: int
    other: int
    update_info: shared.UpdateInfo

    def __init__(self,
                 order_id:  order.OrderId,
                 sort_id: int,
                 container_id: container.ContainerId,
                 freight: int,
                 surcharge: int,
                 other: int,
                 update_info: shared.UpdateInfo):
        self.order_id = order_id
        self.sort_id = sort_id
        self.container_id = container_id
        self.freight = freight
        self.surcharge = surcharge
        self.other = other
        self.update_info = update_info
