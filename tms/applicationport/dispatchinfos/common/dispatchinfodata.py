from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, eq=True)
class DispatchInfoData:
    container_id: str
    day: str
    index: int
    order_id: str
    working_type: int
    contractor_type: int
    driver_code: str
    vehicle_number: str
    departure_point: str
    arrival_point: str
    sales: int
    cost: int
    remark: str
    create_user: str
    update_user: str
    create_at: str
    update_at: str

    def __init__(self,
                 container_id: str,
                 day: datetime,
                 index: int,
                 order_id: str,
                 working_type: int,
                 contractor_type: int,
                 driver_code: str,
                 vehicle_number: str,
                 departure_point: str,
                 arrival_point: str,
                 sales: int,
                 cost: int,
                 remark: str,
                 create_user: str,
                 update_user: str,
                 create_at: datetime,
                 update_at: datetime):
        self.container_id = container_id
        self.day = day
        self.index = index
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
