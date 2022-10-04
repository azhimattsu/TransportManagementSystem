from typing import Optional

from tms.domain.valueobjects import order
from tms.domain.entities.orderinfo import OrderInfoEntity
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository

import tms.mysqlinfrastructure.schemas.orderinfo as c
import tms.mysqlinfrastructure.mysql_setting as s


class MySqlOrderInfos(OrderInfosRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[OrderInfoEntity]:
        results: list[OrderInfoEntity] = []
        results.clear()

        rows = s.session.query(c.OrderInfos).all()
        for row in rows:
            results.append(c.to_entity(row))

        return results

    def find_data_bycode(self,
                         code: order.slicpcode) -> Optional[OrderInfoEntity]:
        row = s.session.query(c.OrderInfos).filter(c.OrderInfos.slip_code == code.value).first()
        if row is None:
            return None

        return c.to_entity(row)

    def find_data_byid(self, id: order.id) -> Optional[OrderInfoEntity]:
        row = s.session.query(c.OrderInfos).filter(c.OrderInfos.order_id == id.value).first()
        if row is None:
            return None

    def create_data(self, orderinfo: OrderInfoEntity):
        s.session.begin()
        row = c.from_entity(orderinfo)
        s.session.add(row)
        s.session.commit()

    def update_data(self, orderinfo: OrderInfoEntity):
        s.session.begin()
        found = s.session.query(c.OrderInfos).filter(c.OrderInfos.order_id == orderinfo.order_id.value).first()
        if found is None:
            return

        found.import_entity(orderinfo)
        s.session.commit()
