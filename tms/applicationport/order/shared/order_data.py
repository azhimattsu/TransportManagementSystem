import copy
from dataclasses import dataclass
from .order_detail_data import OrderDetailData
from .order_container_data import OrderContainerData


@dataclass(init=False, eq=True)
class OrderData:
    detail: OrderDetailData
    containers: list[OrderContainerData]

    def __init__(self,
                 detail: OrderDetailData,
                 containers: list[OrderContainerData]):
        self.detail = copy.deepcopy(detail)
        self.containers = copy.deepcopy(containers)
