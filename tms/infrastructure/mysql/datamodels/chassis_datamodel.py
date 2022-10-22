from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp

from tms.infrastructure.mysql.mysql_setting import Base

from tms.domain.models import chassis
from tms.domain.models import shared


class ChassisDataModel(Base):
    __tablename__ = "chassis"
    chassis_id = Column(String(64), primary_key=True, nullable=False)
    chassis_code = Column(String(10), nullable=False)
    vehicle_number = Column(String(7), nullable=False)
    size = Column(Integer, nullable=False)
    axes = Column(Integer, nullable=False)
    inspection_expired = Column(DateTime, nullable=False)
    model = Column(String(32), nullable=False)
    create_user = Column(String(60))
    update_user = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def import_entity(self, entity: chassis.ChassisInfo):
        self.chassis_id = entity.chassis_id.value
        self.chassis_code = entity.chassis_code.value
        self.vehicle_number = entity.vehicle_number.value
        self.size = entity.size.value
        self.axes = entity.axes.value
        self.inspection_expired = entity.inspection_expired.value
        self.model = entity.model.value
        self.create_user = entity.update_info.create_user.value
        self.update_user = entity.update_info.update_user.value


def from_entity(entity: chassis.ChassisInfo) -> ChassisDataModel:
    target = ChassisDataModel()
    target.import_entity(entity)
    return target


def to_entity(row: ChassisDataModel) -> chassis.ChassisInfo:
    target = chassis.ChassisInfo(chassis.ChassisId(row.chassis_id),
                                 chassis.ChassisCode(row.chassis_code),
                                 chassis.VehicleNumber(row.vehicle_number),
                                 chassis.Size(row.size),
                                 chassis.Axes(row.axes),
                                 shared.CDateTime(row.inspection_expired),
                                 chassis.Model(row.model),
                                 shared.UpdateInfo(shared.MailAddress(row.create_user),
                                                   shared.MailAddress(row.update_user),
                                                   shared.CDateTime(row.create_at),
                                                   shared.CDateTime(row.update_at)))
    return target
