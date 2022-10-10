from dataclasses import dataclass
from tms.domain.valueobjects import container
from tms.domain.valueobjects import dispatch
from tms.domain.valueobjects import common
from tms.domain.valueobjects import order


@dataclass(init=False, eq=True)
class DispatchInfoEntity:
    container_id: container.Id
    day: common.CDateTime
    sort_id: int
    order_id: order.Id
    working_type: dispatch.WorkingType
    contractor_type: dispatch.ContractorType
    driver_code: dispatch.DriverCode
    vehicle_number: dispatch.VehicleNumber
    departure_point: dispatch.PointCode
    arrival_point: dispatch.PointCode
    sales: int
    cost: int
    remark: dispatch.Remark
    create_user: common.MailAddress
    update_user: common.MailAddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 container_id: container.Id,
                 day: common.CDateTime,
                 sort_id: int,
                 order_id: order.Id,
                 working_type: dispatch.WorkingType,
                 contractor_type: dispatch.ContractorType,
                 driver_code: dispatch.DriverCode,
                 vehicle_number: dispatch.VehicleNumber,
                 departure_point: dispatch.PointCode,
                 arrival_point: dispatch.PointCode,
                 sales: int,
                 cost: int,
                 remark: dispatch.Remark,
                 create_user: common.MailAddress,
                 update_user: common.MailAddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):

        self.container_id = container_id
        self.day = day
        self.sort_id = sort_id
        self.order_id = order_id
        self.working_type = working_type
        self.contractor_type = contractor_type
        self.driver_code = driver_code
        self.vehicle_number = vehicle_number
        self.departure_point = departure_point
        self.arrival_point = arrival_point
        self.sales = sales
        self.cost = cost
        self.remark = remark
        self.create_user = create_user
        self.update_user = update_user
        self.create_at = create_at
        self.update_at = update_at
