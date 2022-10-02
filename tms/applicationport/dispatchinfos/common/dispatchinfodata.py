from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, eq=True)
class DispatchInfoData:
    containerId: str
    day: str
    index: int
    orderinfoId: str
    workingtype: int
    contractortype: int
    drivercode: str
    vehiclenumber: str
    departurepoint: str
    arrivalpoint: str
    sales: int
    cost: int
    remark: str
    createuser: str
    updateuser: str
    create_at: str
    update_at: str

    def __init__(self,
                 containerId: str,
                 day: datetime,
                 index: int,
                 orderinfoId: str,
                 workingtype: int,
                 contractortype: int,
                 drivercode: str,
                 vehiclenumber: str,
                 departurepoint: str,
                 arrivalpoint: str,
                 sales: int,
                 cost: int,
                 remark: str,
                 createuser: str,
                 updateuser: str,
                 create_at: datetime,
                 update_at: datetime):
        self.containerId = containerId
        self.day = day
        self.index = index
        self.orderinfoId = orderinfoId
        self.workingtype = workingtype
        self.contractortype = contractortype
        self.drivercode = drivercode
        self.vehiclenumber = vehiclenumber
        self.departurepoint = departurepoint
        self.arrivalpoint = arrivalpoint
        self.sales = sales
        self.cost = cost
        self.remark = remark
        self.createuser = createuser
        self.updateuser = updateuser
        self.create_at = create_at
        self.update_at = update_at
