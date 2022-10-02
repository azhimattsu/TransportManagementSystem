from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp
from tms.domain.valueobjects.common.cdatetime import CDateTime
from tms.mysqlinfrastructure.mysql_setting import Base
from tms.domain.entities.orderinfo import OrderInfoEntity
from tms.domain.valueobjects import common, order


class OrderInfos(Base):
    __tablename__ = "orderinfo"
    id = Column(String(64), primary_key=True, nullable=False)
    slipcode = Column(String(10), nullable=False)
    customercode = Column(String(10), nullable=False)
    customername = Column(String(40), nullable=False)
    salesofficecode = Column(String(10), nullable=False)
    salesofficename = Column(String(40), nullable=False)
    loadingdate = Column(DateTime, default=datetime.utcnow)
    carryindate = Column(DateTime, default=datetime.utcnow)
    billingdate = Column(DateTime, default=datetime.utcnow)
    loadingareacode = Column(String(10), nullable=False)
    loadingareaname = Column(String(40), nullable=False)
    loadingareaphone = Column(String(11), nullable=False)
    loadingareaaddress1 = Column(String(60), nullable=False)
    loadingareaaddress2 = Column(String(60), nullable=False)
    workingareacode = Column(String(10), nullable=False)
    workingareaname = Column(String(40), nullable=False)
    workingareaphone = Column(String(11), nullable=False)
    workingareaaddress1 = Column(String(60), nullable=False)
    workingareaaddress2 = Column(String(60), nullable=False)
    carryinareacode = Column(String(10), nullable=False)
    carryinareaname = Column(String(40), nullable=False)
    carryinareaphone = Column(String(11), nullable=False)
    carryinareaaddress1 = Column(String(60), nullable=False)
    carryinareaaddress2 = Column(String(60), nullable=False)
    remark = Column(String(60), nullable=False)
    destinataioncode = Column(String(10), nullable=False)
    destinataionname = Column(String(40), nullable=False)
    createuser = Column(String(60))
    updateuser = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def import_entity(self, entity: OrderInfoEntity):
        self.id = entity.id.value
        self.slipcode = entity.slipcode.value
        self.customercode = entity.customercode.value
        self.customername = entity.customername.value
        self.salesofficecode = entity.salesofficecode.value
        self.salesofficename = entity.salesofficename.value
        self.loadingdate = entity.loadingdate.value
        self.carryindate = entity.carryindate.value
        self.billingdate = entity.billingdate.value
        self.loadingareacode = entity.loadingareacode.value
        self.loadingareaname = entity.loadingareaname.value
        self.loadingareaphone = entity.loadingareaphone.value
        self.loadingareaaddress1 = entity.loadingareaaddress1.value
        self.loadingareaaddress2 = entity.loadingareaaddress2.value
        self.workingareacode = entity.workingareacode.value
        self.workingareaname = entity.workingareaname.value
        self.workingareaphone = entity.workingareaphone.value
        self.workingareaaddress1 = entity.workingareaaddress1.value
        self.workingareaaddress2 = entity.workingareaaddress2.value
        self.carryinareacode = entity.carryinareacode.value
        self.carryinareaname = entity.carryinareaname.value
        self.carryinareaphone = entity.carryinareaphone.value
        self.carryinareaaddress1 = entity.carryinareaaddress1.value
        self.carryinareaaddress2 = entity.carryinareaaddress2.value
        self.remark = entity.remark.value
        self.destinataioncode = entity.destinataioncode.value
        self.destinataionname = entity.destinataionname.value
        self.createuser = entity.createuser.value
        self.updateuser = entity.updateuser.value


def from_entity(entity: OrderInfoEntity) -> OrderInfos:
    target = OrderInfos()
    target.id = entity.id.value
    target.slipcode = entity.slipcode.value
    target.customercode = entity.customercode.value
    target.customername = entity.customername.value
    target.salesofficecode = entity.salesofficecode.value
    target.salesofficename = entity.salesofficename.value
    target.loadingdate = entity.loadingdate.value
    target.carryindate = entity.carryindate.value
    target.billingdate = entity.billingdate.value
    target.loadingareacode = entity.loadingareacode.value
    target.loadingareaname = entity.loadingareaname.value
    target.loadingareaphone = entity.loadingareaphone.value
    target.loadingareaaddress1 = entity.loadingareaaddress1.value
    target.loadingareaaddress2 = entity.loadingareaaddress2.value
    target.workingareacode = entity.workingareacode.value
    target.workingareaname = entity.workingareaname.value
    target.workingareaphone = entity.workingareaphone.value
    target.workingareaaddress1 = entity.workingareaaddress1.value
    target.workingareaaddress2 = entity.workingareaaddress2.value
    target.carryinareacode = entity.carryinareacode.value
    target.carryinareaname = entity.carryinareaname.value
    target.carryinareaphone = entity.carryinareaphone.value
    target.carryinareaaddress1 = entity.carryinareaaddress1.value
    target.carryinareaaddress2 = entity.carryinareaaddress2.value
    target.remark = entity.remark.value
    target.destinataioncode = entity.destinataioncode.value
    target.destinataionname = entity.destinataionname.value
    target.createuser = entity.createuser.value
    target.updateuser = entity.updateuser.value

    return target


def to_entity(row: OrderInfos) -> OrderInfoEntity:
    target = OrderInfoEntity(order.Id(row.id),
                             order.SlipCode(row.slipcode),
                             order.CustomerCode(row.customercode),
                             order.Name(row.customername),
                             order.SalesOfficeCode(row.salesofficecode),
                             order.Name(row.salesofficename),
                             CDateTime(row.loadingdate),
                             CDateTime(row.carryindate),
                             CDateTime(row.billingdate),
                             order.LoadingAreaCode(row.loadingareacode),
                             order.Name(row.loadingareaname),
                             order.PhoneNumber(row.loadingareaphone),
                             order.Address(row.loadingareaaddress1),
                             order.Address(row.loadingareaaddress2),
                             order.WorkingAreaCode(row.workingareacode),
                             order.Name(row.workingareaname),
                             order.PhoneNumber(row.workingareaphone),
                             order.Address(row.workingareaaddress1),
                             order.Address(row.workingareaaddress2),
                             order.CarryInAreaCode(row.carryinareacode),
                             order.Name(row.carryinareaname),
                             order.PhoneNumber(row.carryinareaphone),
                             order.Address(row.carryinareaaddress1),
                             order.Address(row.carryinareaaddress2),
                             order.Remark(row.remark),
                             order.DestinationCode(row.destinataioncode),
                             order.Name(row.destinataionname),
                             common.MailAddress(row.createuser),
                             common.MailAddress(row.updateuser),
                             CDateTime(row.create_at),
                             CDateTime(row.update_at))

    return target
