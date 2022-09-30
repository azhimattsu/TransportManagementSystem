from dataclasses import dataclass

from tms.domain.valueobjects import common, order


@dataclass(init=False, eq=True)
class OrderInfoEntity:
    id: order.Id
    slipcode: order.SlipCode
    customercode: order.CustomerCode
    customername: order.Name
    salesofficecode: order.SalesOfficeCode
    salesofficename: order.Name
    loadingdate: common.CDateTime
    carryindate: common.CDateTime
    billingdate: common.CDateTime
    loadingareacode: order.LoadingAreaCode
    loadingareaname: order.Name
    loadingareaphone: order.PhoneNumber
    loadingareaaddress1: order.Address
    loadingareaaddress2: order.Address
    workingareacode: order.WorkingAreaCode
    workingareaname: order.Name
    workingareaphone: order.PhoneNumber
    workingareaaddress1: order.Address
    workingareaaddress2: order.Address
    carryinareacode: order.CarryInAreaCode
    carryinareaname: order.Name
    carryinareaphone: order.PhoneNumber
    carryinareaaddress1: order.Address
    carryinareaaddress2: order.Address
    remark: order.Remark
    destinataioncode: order.DestinationCode
    destinataionname: order.Name
    createuser: common.MailAddress
    updateuser: common.MailAddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 id: order.Id,
                 slipcode: order.SlipCode,
                 customercode: order.CustomerCode,
                 customername: order.Name,
                 salesofficecode: order.SalesOfficeCode,
                 salesofficename: order.Name,
                 loadingdate: common.CDateTime,
                 carryindate: common.CDateTime,
                 billingdate: common.CDateTime,
                 loadingareacode: order.LoadingAreaCode,
                 loadingareaname: order.Name,
                 loadingareaphone: order.PhoneNumber,
                 loadingareaaddress1: order.Address,
                 loadingareaaddress2: order.Address,
                 workingareacode: order.WorkingAreaCode,
                 workingareaname: order.Name,
                 workingareaphone: order.PhoneNumber,
                 workingareaaddress1: order.Address,
                 workingareaaddress2: order.Address,
                 carryinareacode: order.CarryInAreaCode,
                 carryinareaname: order.Name,
                 carryinareaphone: order.PhoneNumber,
                 carryinareaaddress1: order.Address,
                 carryinareaaddress2: order.Address,
                 remark: order.Remark,
                 destinataioncode: order.DestinationCode,
                 destinataionname: order.Name,
                 createuser: common.MailAddress,
                 updateuser: common.MailAddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):
        self.id = id
        self.slipcode = slipcode
        self.customercode = customercode
        self.customername = customername
        self.salesofficecode = salesofficecode
        self.salesofficename = salesofficename
        self.loadingdate = loadingdate
        self.carryindate = carryindate
        self.billingdate = billingdate
        self.loadingareacode = loadingareacode
        self.loadingareaname = loadingareaname
        self.loadingareaphone = loadingareaphone
        self.loadingareaaddress1 = loadingareaaddress1
        self.loadingareaaddress2 = loadingareaaddress2
        self.workingareacode = workingareacode
        self.workingareaname = workingareaname
        self.workingareaphone = workingareaphone
        self.workingareaaddress1 = workingareaaddress1
        self.workingareaaddress2 = workingareaaddress2
        self.carryinareacode = carryinareacode
        self.carryinareaname = carryinareaname
        self.carryinareaphone = carryinareaphone
        self.carryinareaaddress1 = carryinareaaddress1
        self.carryinareaaddress2 = carryinareaaddress2
        self.remark = remark
        self.destinataioncode = destinataioncode
        self.destinataionname = destinataionname
        self.createuser = createuser
        self.updateuser = updateuser
        self.create_at = create_at
        self.update_at = update_at
