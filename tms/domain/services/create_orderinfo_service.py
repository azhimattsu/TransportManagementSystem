
from tms.domain.valueobjects import order
import uuid


class CreateOrderInfoService:

    @staticmethod
    def get_orderInfoid() -> order.Id:
        return order.Id(str(uuid.uuid4()))
