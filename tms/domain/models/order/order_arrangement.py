import copy
from dataclasses import dataclass
from tms.domain.models import order


@dataclass(init=False, eq=True)
class OrderArrangement:
    order_id: order.OrderId
    containers: list[order.ContainerRow]

    def __init__(self, order_id: order.OrderId, containers: list[order.ContainerRow]):
        self.order_id = order_id
        self.containers = copy.deepcopy(containers)
