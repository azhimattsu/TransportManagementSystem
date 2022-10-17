
from tms.domain.models import order
import uuid


class CreateOrderInfoService:

    @staticmethod
    def get_orderInfoid() -> order.OrderId:
        return order.OrderId(str(uuid.uuid4()))
