import copy
from tms.applicationport.order.shared.order_container_data import OrderContainerData


class OrderContainerPutInputData:
    orderinfo: list[OrderContainerData]

    def __init__(self, orderinfo: list[OrderContainerData]):
        self.orderinfo = copy.deepcopy(orderinfo)

    def get_order_id(self) -> str:
        if len(self.orderinfo) > 0:
            return self.orderinfo[0].order_id
