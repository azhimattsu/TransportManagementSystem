from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp
from tms.domain.valueobjects import common, dispatch, order
from tms.mysqlinfrastructure.mysql_setting import Base
from tms.domain.entities.dispatchinfo import DispatchInfoEntity
from tms.domain.valueobjects import container


class DispatchInfo(Base):
    __tablename__ = "dispatchinfo"
    container_id = Column(String(64), primary_key=True, nullable=False)
    day = Column(DateTime, primary_key=True, default=datetime.utcnow)
    sort_id = Column(Integer, primary_key=True, nullable=False)
    order_id = Column(String(64), nullable=False)
    working_type = Column(Integer, nullable=False)
    contractor_type = Column(Integer, nullable=False)
    driver_code = Column(String(10), nullable=False)
    vehicle_number = Column(String(10), nullable=False)
    departure_point = Column(String(10), nullable=False)
    arrival_point = Column(String(10), nullable=False)
    sales = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    remark = Column(String(60), nullable=False)
    create_user = Column(String(60))
    update_user = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def import_entity(self, entity: DispatchInfoEntity):
        self.container_id = entity.container_id.value
        self.day = entity.day.value
        self.sort_id = entity.sort_id
        self.order_id = entity.order_id.value
        self.working_type = int(entity.working_type)
        self.contractor_type = int(entity.contractor_type)
        self.driver_code = entity.driver_code.value
        self.vehicle_number = entity.vehicle_number.value
        self.departure_point = entity.departure_point.value
        self.arrival_point = entity.arrival_point.value
        self.sales = entity.sales
        self.cost = entity.cost
        self.remark = entity.remark.value
        self.create_user = entity.create_user.value
        self.update_user = entity.update_user.value


def from_entity(entity: DispatchInfoEntity) -> DispatchInfo:
    print(entity)
    target = DispatchInfo()
    target.container_id = entity.container_id.value
    target.day = entity.day.value
    target.sort_id = entity.sort_id
    target.order_id = entity.order_id.value
    target.working_type = int(entity.working_type)
    target.contractor_type = int(entity.contractor_type)
    target.driver_code = entity.driver_code.value
    target.vehicle_number = entity.vehicle_number.value
    target.departure_point = entity.departure_point.value
    target.arrival_point = entity.arrival_point.value
    target.sales = entity.sales
    target.cost = entity.cost
    target.remark = entity.remark.value
    target.create_user = entity.create_user.value
    target.update_user = entity.update_user.value
    return target


def to_entity(row: DispatchInfo) -> DispatchInfoEntity:
    target = DispatchInfoEntity(container.Id(row.container_id),
                                common.CDateTime(row.day),
                                row.sort_id,
                                order.Id(row.order_id),
                                dispatch.WorkingType(row.working_type),
                                dispatch.ContractorType(row.contractor_type),
                                dispatch.DriverCode(row.driver_code),
                                dispatch.VehicleNumber(row.vehicle_number),
                                dispatch.PointCode(row.departure_point),
                                dispatch.PointCode(row.arrival_point),
                                row.sales,
                                row.cost,
                                dispatch.Remark(row.remark),
                                common.MailAddress(row.create_user),
                                common.MailAddress(row.update_user),
                                common.CDateTime(row.create_at),
                                common.CDateTime(row.update_at))
    return target
