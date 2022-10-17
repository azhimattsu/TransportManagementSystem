from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp

from tms.infrastructure.mysql.mysql_setting import Base

from tms.domain.models import customer
from tms.domain.models import distinations
from tms.domain.models import order
from tms.domain.models import salesoffice
from tms.domain.models import shared


class OrderDetailDataModel(Base):
    __tablename__ = "order_detail"
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

    def import_entity(self, entity: order.OrderDetail):
        self.order_id = entity.order_id.value
        self.slip_code = entity.slip_code.value
        self.customer_code = entity.customer_info.code.value
        self.customer_name = entity.customer_info.name.value
        self.salesoffice_code = entity.salesoffice_info.code.value
        self.salesoffice_name = entity.salesoffice_info.name.value
        self.loading_date = entity.loading_date.value
        self.carryin_date = entity.carryin_date.value
        self.billing_date = entity.billing_date.value
        self.loading_area_code = entity.loading_area_info.code.value
        self.loading_area_name = entity.loading_area_info.name.value
        self.loading_area_phone = entity.loading_area_info.phone.value
        self.loading_area_address1 = entity.loading_area_info.address1.value
        self.loading_area_address2 = entity.loading_area_info.address2.value
        self.working_area_code = entity.working_area_info.code.value
        self.working_area_name = entity.working_area_info.name.value
        self.working_area_phone = entity.working_area_info.phone.value
        self.working_area_address1 = entity.working_area_info.address1.value
        self.working_area_address2 = entity.working_area_info.address2.value
        self.carryin_area_code = entity.carryin_area_info.code.value
        self.carryin_area_name = entity.carryin_area_info.name.value
        self.carryin_area_phone = entity.carryin_area_info.phone.value
        self.carryin_area_address1 = entity.carryin_area_info.address1.value
        self.carryin_area_address2 = entity.carryin_area_info.address2.value
        self.remark = entity.remark.value
        self.destinataion_code = entity.destinataion_info.code.value
        self.destinataion_name = entity.carryin_area_info.name.value
        self.create_user = entity.update_info.create_user.value
        self.update_user = entity.update_info.update_user.value


def from_entity(entity: order.OrderDetail) -> OrderDetailDataModel:
    target = OrderDetailDataModel()
    target.import_entity(entity)

    return target


def to_entity(row: OrderDetailDataModel) -> order.OrderDetail:
    target = order.OrderDetail(order.OrderId(row.order_id),
                               order.SlipCode(row.slip_code),
                               customer.CustomerInfo(customer.CustomerCode(row.customer_code),
                                                     customer.CustomerName(row.customer_name)),
                               salesoffice.SalesOfficeInfo(salesoffice.SalesOfficeCode(row.salesoffice_code),
                                                           salesoffice.SalesOfficeName(row.salesoffice_name)),
                               shared.CDateTime(row.loading_date),
                               shared.CDateTime(row.carryin_date),
                               shared.CDateTime(row.billing_date),
                               order.PlaceInfo(order.PlaceCode(row.loading_area_code),
                                               order.PlaceName(row.loading_area_name),
                                               shared.PhoneNumber(row.loading_area_phone),
                                               shared.Address(row.loading_area_address1),
                                               shared.Address(row.loading_area_address2)),
                               order.PlaceInfo(order.PlaceCode(row.working_area_code),
                                               order.PlaceName(row.working_area_name),
                                               shared.PhoneNumber(row.working_area_phone),
                                               shared.Address(row.working_area_address1),
                                               shared.Address(row.working_area_address2)),
                               order.PlaceInfo(order.PlaceCode(row.carryin_area_code),
                                               order.PlaceName(row.carryin_area_name),
                                               shared.PhoneNumber(row.carryin_area_phone),
                                               shared.Address(row.working_area_address1),
                                               shared.Address(row.carryin_area_address2)),
                               shared.Remark(row.remark),
                               distinations.DistinationInfo(distinations.DistinationCode(row.destinataion_code),
                                                            distinations.DistinationName(row.destinataion_name)),
                               shared.UpdateInfo(shared.MailAddress(row.create_user),
                                                 shared.MailAddress(row.update_user),
                                                 shared.CDateTime(row.create_at),
                                                 shared.CDateTime(row.update_at)))
    return target
