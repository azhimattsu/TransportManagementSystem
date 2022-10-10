from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp
from tms.domain.valueobjects import common, order
from tms.mysqlinfrastructure.mysql_setting import Base
from tms.domain.entities.orderinfo_container import OrderInfoContainerEntity
from tms.domain.valueobjects import container


class OrderInfoContainer(Base):
    __tablename__ = "orderinfo_container"
    order_id = Column(String(64), primary_key=True, nullable=False)
    sort_id = Column(Integer, primary_key=True, nullable=False)
    container_id = Column(String(64), nullable=False)
    freight = Column(Integer, nullable=False)
    surcharge = Column(Integer, nullable=False)
    other = Column(Integer, nullable=False)
    create_user = Column(String(60))
    update_user = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def import_entity(self, entity: OrderInfoContainerEntity):
        self.order_id = entity.order_id.value
        self.sort_id = entity.sort_id
        self.container_id = entity.container_id.value
        self.freight = entity.freight
        self.surcharge = entity.surcharge
        self.other = entity.other
        self.create_user = entity.create_user.value
        self.update_user = entity.update_user.value


def from_entity(entity: OrderInfoContainerEntity) -> OrderInfoContainer:
    target = OrderInfoContainer()
    target.order_id = entity.order_id.value
    target.sort_id = entity.sort_id
    target.container_id = entity.container_id.value
    target.freight = entity.freight
    target.surcharge = entity.surcharge
    target.other = entity.other
    target.create_user = entity.create_user.value
    target.update_user = entity.update_user.value
    return target


def to_entity(row: OrderInfoContainer) -> OrderInfoContainerEntity:
    target = OrderInfoContainerEntity(order.Id(row.order_id),
                                      row.sort_id,
                                      container.Id(row.container_id),
                                      row.freight,
                                      row.surcharge,
                                      row.other,
                                      common.MailAddress(row.create_user),
                                      common.MailAddress(row.update_user),
                                      common.CDateTime(row.create_at),
                                      common.CDateTime(row.update_at))
    return target
