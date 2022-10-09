import copy
from dataclasses import dataclass
from .orderinfo_basedata import OrderInfoBaseData
from .orderinfo_containerdata import OrderInfoContainerData


@dataclass(init=False, eq=True)
class OrderInfoData:
    info: OrderInfoBaseData
    containers: list[OrderInfoContainerData]

    def __init__(self,
                 info: OrderInfoBaseData,
                 containers: list[OrderInfoContainerData]):
        self.info = copy.deepcopy(info)
        self.containers = copy.deepcopy(containers)
