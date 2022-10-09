from typing import Optional
from tms.domain.entities.orderinfo import OrderInfoEntity
from tms.domain.entities.orderinfo_container import OrderInfoContainerEntity

from tms.domain.valueobjects import order
from tms.domain.entities.orderinfo_base import OrderInfoBaseEntity
from tms.domain.repositories.orderinfo_repository import OrderInfosRepository

import tms.mysqlinfrastructure.schemas.orderinfo_base as ob
import tms.mysqlinfrastructure.schemas.orderinfo_container as oc

import tms.mysqlinfrastructure.mysql_setting as s


class MySqlOrderInfos(OrderInfosRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[OrderInfoBaseEntity]:
        results: list[OrderInfoBaseEntity] = []
        results.clear()

        rows = s.session.query(ob.OrderInfoBase).all()
        for row in rows:
            results.append(ob.to_entity(row))

        return results

    def find_data_bycode(self,
                         code: order.SlipCode) -> Optional[OrderInfoBaseEntity]:
        row = s.session.query(ob.OrderInfoBase).filter(ob.OrderInfoBase.slip_code == code.value).first()
        if row is None:
            return None

        return ob.to_entity(row)

    def find_data_byid(self, id: order.Id) -> Optional[OrderInfoBaseEntity]:
        row = s.session.query(ob.OrderInfoBase).filter(ob.OrderInfoBase.order_id == id.value).first()
        if row is None:
            return None

        return ob.to_entity(row)

    def create_data(self, orderinfo: OrderInfoBaseEntity):
        s.session.begin()
        row = ob.from_entity(orderinfo)
        s.session.add(row)
        s.session.commit()

    def update_data(self, orderinfo: OrderInfoBaseEntity):
        s.session.begin()
        found = s.session.query(ob.OrderInfoBase).filter(ob.OrderInfoBase.order_id == orderinfo.order_id.value).first()
        if found is None:
            return

        found.import_entity(orderinfo)
        s.session.commit()

    def fetch_container_data_byorderid(self, id: order.Id) -> list[OrderInfoContainerEntity]:
        results: list[OrderInfoContainerEntity] = []
        results.clear()

        rows = s.session.query(oc.OrderInfoContainer).filter(oc.OrderInfoContainer.order_id == id.value).all()
        for row in rows:
            results.append(oc.to_entity(row))

        return results

    def find_fulldata_bycode(self, code: order.SlipCode) -> Optional[OrderInfoEntity]:

        entity_order = self.find_data_bycode(code)
        if entity_order is None:
            return None

        entity_containers: list[OrderInfoContainerEntity] = []
        entity_containers = self.fetch_container_data_byorderid(entity_order.order_id)

        return OrderInfoEntity(entity_order, entity_containers)
