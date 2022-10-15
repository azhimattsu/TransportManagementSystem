from typing import Optional

from tms.domain.models import order

from tms.domain.models.order.order_repository import OrderRepository

import tms.infrastructure.mysql.mysql_setting as settings
import tms.infrastructure.mysql.datamodels.order_detail_datamodel as ob
import tms.infrastructure.mysql.datamodels.order_container_datamodel as oc


class MySqlOrder(OrderRepository):

    def __init__(self):
        pass

    def find_data_bycode(self,
                         code: order.SlipCode) -> Optional[order.OrderInfo]:

        row = settings.session.query(ob.OrderDetailDataModel).filter(ob.OrderDetailDataModel.slip_code == code.value).first()
        if row is None:
            return None

        detail = ob.to_entity(row)

        print("step2")
        arrangements = self.find_container_data_byorderid(detail.order_id)

        return order.OrderInfo(detail.order_id, detail.slip_code, detail, arrangements)

    def find_container_data_byorderid(self, id: order.OrderId) -> Optional[order.OrderArrangement]:
        targets: list[order.ContainerRow] = []
        targets.clear()

        rows = settings.session.query(oc.OrderContainerDataModel).filter(oc.OrderContainerDataModel.order_id == id.value).all()
        for row in rows:
            targets.append(oc.to_entity(row))

        return order.OrderArrangement(id, targets)

    def create_data(self, orderinfo: order.OrderInfo):
        pass

    def update_data(self, orderinfo: order.OrderInfo):
        pass
