from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp

from tms.infrastructure.mysql.mysql_setting import Base

from tms.domain.models import container
from tms.domain.models import order
from tms.domain.models import shared


class OrderContainerDataModel(Base):
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

    def import_entity(self, entity: order.ContainerRow):
        self.order_id = entity.order_id.value
        self.sort_id = entity.sort_id
        self.container_id = entity.container_id.value
        self.freight = entity.freight
        self.surcharge = entity.surcharge
        self.other = entity.other
        self.create_user = entity.update_info.create_user.value
        self.update_user = entity.update_info.update_user.value


def from_entity(entity: order.ContainerRow) -> OrderContainerDataModel:
    target = OrderContainerDataModel()
    target.import_entity(entity)
    return target


def to_entity(row: OrderContainerDataModel) -> order.ContainerRow:
    target = order.ContainerRow(order.OrderId(row.order_id),
                                row.sort_id,
                                container.ContainerId(row.container_id),
                                row.freight,
                                row.surcharge,
                                row.other,
                                shared.UpdateInfo(shared.MailAddress(row.create_user),
                                                  shared.MailAddress(row.update_user),
                                                  shared.CDateTime(row.create_at),
                                                  shared.CDateTime(row.update_at)))
    return target
