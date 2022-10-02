from dataclasses import dataclass
from tms.domain.valueobjects import container
from tms.domain.valueobjects import dispatch
from tms.domain.valueobjects import common
from tms.domain.valueobjects import order


@dataclass(init=False, eq=True)
class DispatchInfoEntity:
    containerId: container.Id
    day: common.CDateTime
    index: int
    orderinfoId: order.Id
    workingtype: dispatch.WorkingType
    contractortype: dispatch.ContractorType
    drivercode: dispatch.DriverCode
    vehiclenumber: dispatch.VehicleNumber
    departurepoint: dispatch.PointCode
    arrivalpoint: dispatch.PointCode
    sales: int
    cost: int
    remark: dispatch.Remark
    createuser: common.MailAddress
    updateuser: common.MailAddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 containerId: container.Id,
                 day: common.CDateTime,
                 index: int,
                 orderinfoId: order.Id,
                 workingtype: dispatch.WorkingType,
                 contractortype: dispatch.ContractorType,
                 drivercode: dispatch.DriverCode,
                 vehiclenumber: dispatch.VehicleNumber,
                 departurepoint: dispatch.PointCode,
                 arrivalpoint: dispatch.PointCode,
                 sales: int,
                 cost: int,
                 remark: dispatch.Remark,
                 createuser: common.MailAddress,
                 updateuser: common.MailAddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):

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
