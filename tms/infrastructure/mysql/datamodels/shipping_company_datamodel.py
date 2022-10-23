from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp

from tms.infrastructure.mysql.mysql_setting import Base

from tms.domain.models import shipping_company
from tms.domain.models import shared


class ShippingCompanyDataModel(Base):
    __tablename__ = "shippingcompany"
    shipping_company_id = Column(String(64), primary_key=True, nullable=False)
    shipping_company_code = Column(String(10), nullable=False)
    shipping_company_name = Column(String(32), nullable=False)
    create_user = Column(String(60))
    update_user = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def import_entity(self, entity: shipping_company.ShippingCompanyInfo):
        self.shipping_company_id = entity.shipping_company_id.value
        self.shipping_company_code = entity.shipping_company_code.value
        self.shipping_company_name = entity.shipping_company_name.value
        self.create_user = entity.update_info.create_user.value
        self.update_user = entity.update_info.update_user.value


def from_entity(entity: shipping_company.ShippingCompanyInfo) -> ShippingCompanyDataModel:
    target = ShippingCompanyDataModel()
    target.import_entity(entity)
    return target


def to_entity(row: ShippingCompanyDataModel) -> shipping_company.ShippingCompanyInfo:
    target = shipping_company.ShippingCompanyInfo(shipping_company.ShippingCompanyId(row.shipping_company_id),
                                                  shipping_company.ShippingCompanyCode(row.shipping_company_code),
                                                  shipping_company.ShippingCompanyName(row.shipping_company_name),
                                                  shared.UpdateInfo(shared.MailAddress(row.create_user),
                                                                    shared.MailAddress(row.update_user),
                                                                    shared.CDateTime(row.create_at),
                                                                    shared.CDateTime(row.update_at)))
    return target
