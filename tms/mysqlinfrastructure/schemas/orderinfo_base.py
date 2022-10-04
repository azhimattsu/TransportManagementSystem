from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp
from tms.domain.valueobjects.common.cdatetime import CDateTime
from tms.mysqlinfrastructure.mysql_setting import Base
from tms.domain.entities.orderinfo_base import OrderInfoBaseEntity
from tms.domain.valueobjects import common, order


class OrderInfoBase(Base):
    __tablename__ = "orderinfo_base"
    order_id = Column(String(64), primary_key=True, nullable=False)
    slip_code = Column(String(10), nullable=False)
    customer_code = Column(String(10), nullable=False)
    customer_name = Column(String(40), nullable=False)
    salesoffice_code = Column(String(10), nullable=False)
    salesoffice_name = Column(String(40), nullable=False)
    loading_date = Column(DateTime, default=datetime.utcnow)
    carryin_date = Column(DateTime, default=datetime.utcnow)
    billing_date = Column(DateTime, default=datetime.utcnow)
    loading_area_code = Column(String(10), nullable=False)
    loading_area_name = Column(String(40), nullable=False)
    loading_area_phone = Column(String(11), nullable=False)
    loading_area_address1 = Column(String(60), nullable=False)
    loading_area_address2 = Column(String(60), nullable=False)
    working_area_code = Column(String(10), nullable=False)
    working_area_name = Column(String(40), nullable=False)
    working_area_phone = Column(String(11), nullable=False)
    working_area_address1 = Column(String(60), nullable=False)
    working_area_address2 = Column(String(60), nullable=False)
    carryin_area_code = Column(String(10), nullable=False)
    carryin_area_name = Column(String(40), nullable=False)
    carryin_area_phone = Column(String(11), nullable=False)
    carryin_area_address1 = Column(String(60), nullable=False)
    carryin_area_address2 = Column(String(60), nullable=False)
    remark = Column(String(60), nullable=False)
    destinataion_code = Column(String(10), nullable=False)
    destinataion_name = Column(String(40), nullable=False)
    create_user = Column(String(60))
    update_user = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def import_entity(self, entity: OrderInfoBaseEntity):
        self.order_id = entity.order_id.value
        self.slip_code = entity.slip_code.value
        self.customer_code = entity.customer_code.value
        self.customer_name = entity.customer_name.value
        self.salesoffice_code = entity.salesoffice_code.value
        self.salesoffice_name = entity.salesoffice_name.value
        self.loading_date = entity.loading_date.value
        self.carryin_date = entity.carryin_date.value
        self.billing_date = entity.billing_date.value
        self.loading_area_code = entity.loading_area_code.value
        self.loading_area_name = entity.loading_area_name.value
        self.loading_area_phone = entity.loading_area_phone.value
        self.loading_area_address1 = entity.loading_area_address1.value
        self.loading_area_address2 = entity.loading_area_address2.value
        self.working_area_code = entity.working_area_code.value
        self.working_area_name = entity.working_area_name.value
        self.working_area_phone = entity.working_area_phone.value
        self.working_area_address1 = entity.working_area_address1.value
        self.working_area_address2 = entity.working_area_address2.value
        self.carryin_area_code = entity.carryin_area_code.value
        self.carryin_area_name = entity.carryin_area_name.value
        self.carryin_area_phone = entity.carryin_area_phone.value
        self.carryin_area_address1 = entity.carryin_area_address1.value
        self.carryin_area_address2 = entity.carryin_area_address2.value
        self.remark = entity.remark.value
        self.destinataion_code = entity.destinataion_code.value
        self.destinataion_name = entity.destinataion_name.value
        self.create_user = entity.create_user.value
        self.update_user = entity.update_user.value


def from_entity(entity: OrderInfoBaseEntity) -> OrderInfoBase:
    target = OrderInfoBase()
    target.order_id = entity.order_id.value
    target.slip_code = entity.slip_code.value
    target.customer_code = entity.customer_code.value
    target.customer_name = entity.customer_name.value
    target.salesoffice_code = entity.salesoffice_code.value
    target.salesoffice_name = entity.salesoffice_name.value
    target.loading_date = entity.loading_date.value
    target.carryin_date = entity.carryin_date.value
    target.billing_date = entity.billing_date.value
    target.loading_area_code = entity.loading_area_code.value
    target.loading_area_name = entity.loading_area_name.value
    target.loading_area_phone = entity.loading_area_phone.value
    target.loading_area_address1 = entity.loading_area_address1.value
    target.loading_area_address2 = entity.loading_area_address2.value
    target.working_area_code = entity.working_area_code.value
    target.working_area_name = entity.working_area_name.value
    target.working_area_phone = entity.working_area_phone.value
    target.working_area_address1 = entity.working_area_address1.value
    target.working_area_address2 = entity.working_area_address2.value
    target.carryin_area_code = entity.carryin_area_code.value
    target.carryin_area_name = entity.carryin_area_name.value
    target.carryin_area_phone = entity.carryin_area_phone.value
    target.carryin_area_address1 = entity.carryin_area_address1.value
    target.carryin_area_address2 = entity.carryin_area_address2.value
    target.remark = entity.remark.value
    target.destinataion_code = entity.destinataion_code.value
    target.destinataion_name = entity.destinataion_name.value
    target.create_user = entity.create_user.value
    target.update_user = entity.update_user.value

    return target


def to_entity(row: OrderInfoBase) -> OrderInfoBaseEntity:
    target = OrderInfoBaseEntity(order.Id(row.order_id),
                                 order.SlipCode(row.slip_code),
                                 order.CustomerCode(row.customer_code),
                                 order.Name(row.customer_name),
                                 order.SalesOfficeCode(row.salesoffice_code),
                                 order.Name(row.salesoffice_name),
                                 CDateTime(row.loading_date),
                                 CDateTime(row.carryin_date),
                                 CDateTime(row.billing_date),
                                 order.LoadingAreaCode(row.loading_area_code),
                                 order.Name(row.loading_area_name),
                                 order.PhoneNumber(row.loading_area_phone),
                                 order.Address(row.loading_area_address1),
                                 order.Address(row.loading_area_address2),
                                 order.WorkingAreaCode(row.working_area_code),
                                 order.Name(row.working_area_name),
                                 order.PhoneNumber(row.working_area_phone),
                                 order.Address(row.working_area_address1),
                                 order.Address(row.working_area_address2),
                                 order.CarryInAreaCode(row.carryin_area_code),
                                 order.Name(row.carryin_area_name),
                                 order.PhoneNumber(row.carryin_area_phone),
                                 order.Address(row.carryin_area_address1),
                                 order.Address(row.carryin_area_address2),
                                 order.Remark(row.remark),
                                 order.DestinationCode(row.destinataion_code),
                                 order.Name(row.destinataion_name),
                                 common.MailAddress(row.create_user),
                                 common.MailAddress(row.update_user),
                                 CDateTime(row.create_at),
                                 CDateTime(row.update_at))

    return target
