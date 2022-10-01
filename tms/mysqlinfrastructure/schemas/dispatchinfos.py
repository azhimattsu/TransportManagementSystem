from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp
from tms.domain.valueobjects import common, dispatch
from tms.mysqlinfrastructure.mysql_setting import Base
from tms.domain.entities.dispatchinfo import DispatchInfoEntity
from tms.domain.valueobjects import container


class DispatchInfos(Base):
    __tablename__ = "dispatchinfos"
    containerId = Column(String(64), primary_key=True, nullable=False)
    day = Column(DateTime, default=datetime.utcnow)
    index = Column(Integer, nullable=False)
    workingtype = Column(Integer, nullable=False)
    contractortype = Column(Integer, nullable=False)
    drivercode = Column(String(10), nullable=False)
    vehiclenumber = Column(String(10), nullable=False)
    departurepoint = Column(String(10), nullable=False)
    arrivalpoint = Column(String(10), nullable=False)
    sales = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    remark = Column(String(60), nullable=False)
    createuser = Column(String(60))
    updateuser = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def importEntity(self, entity: DispatchInfoEntity):
        self.containerId = entity.containerId.value
        self.day = entity.day
        self.index = entity.index
        self.workingtype = int(entity.workingtype)
        self.contractortype = int(entity.contractortype)
        self.drivercode = entity.drivercode.value
        self.vehiclenumber = entity.vehiclenumber.value
        self.departurepoint = entity.departurepoint.value
        self.arrivalpoint = entity.arrivalpoint.value
        self.sales = entity.sales
        self.cost = entity.cost
        self.remark = entity.remark.value
        self.createuser = entity.createuser.value
        self.updateuser = entity.updateuser.value


def fromEntity(entity: DispatchInfoEntity) -> DispatchInfos:
    target = DispatchInfos()
    target.containerId = entity.containerId.value
    target.day = entity.day
    target.index = entity.index
    target.workingtype = int(entity.workingtype)
    target.contractortype = int(entity.contractortype)
    target.drivercode = entity.drivercode.value
    target.vehiclenumber = entity.vehiclenumber.value
    target.departurepoint = entity.departurepoint
    target.arrivalpoint = entity.arrivalpoint.value
    target.sales = entity.sales
    target.cost = entity.cost
    target.remark = entity.remark.value
    target.createuser = entity.createuser.value
    target.updateuser = entity.updateuser.value
    return target


def toEntity(row: DispatchInfos) -> DispatchInfoEntity:
    target = DispatchInfoEntity(container.Id(row.containerId),
                                common.CDateTime(row.day),
                                row.index,
                                dispatch.WorkingType(row.workingtype),
                                dispatch.ContractorType(row.contractortype),
                                dispatch.DriverCode(row.drivercode),
                                dispatch.VehicleNumber(row.vehiclenumber),
                                dispatch.pointcode(row.departurepoint),
                                dispatch.pointcode(row.arrivalpoint),
                                row.sales,
                                row.cost,
                                dispatch.Remark(row.remark),
                                common.MailAddress(row.createuser),
                                common.MailAddress(row.updateuser),
                                common.CDateTime(row.create_at),
                                common.CDateTime(row.update_at))
    return target
