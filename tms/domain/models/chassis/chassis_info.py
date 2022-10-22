from dataclasses import dataclass

from tms.domain.models import shared
from tms.domain.models import chassis
from tms.domain.models.shared.cdatetime import CDateTime


@dataclass(init=False, eq=True)
class ChassisInfo():
    chassis_id: chassis.chassis_id
    chassis_code: chassis.ChassisId
    vehicle_number: chassis.VehicleNumber
    size: chassis.Size
    axes: chassis.Axes
    inspection_expired: CDateTime
    model: chassis.Model
    update_info: shared.UpdateInfo

    def __init__(self,
                 chassis_id: chassis.chassis_id,
                 chassis_code: chassis.ChassisId,
                 vehicle_number: chassis.VehicleNumber,
                 size: chassis.Size,
                 axes: chassis.Axes,
                 inspection_expired: CDateTime,
                 model: chassis.Model,
                 update_info: shared.UpdateInfo):
        self.chassis_id = chassis_id
        self.chassis_code = chassis_code
        self.vehicle_number = vehicle_number
        self.size = size
        self.axes = axes
        self.inspection_expired = inspection_expired
        self.model = model
        self.update_info = update_info
