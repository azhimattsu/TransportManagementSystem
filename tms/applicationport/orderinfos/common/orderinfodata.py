from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, eq=True)
class OrderInfoData:
    id: str
    slipcode: str
    customercode: str
    customername: str
    salesofficecode: str
    salesofficename: str
    loadingdate: str
    carryindate: str
    billingdate: str
    loadingareacode: str
    loadingareaname: str
    loadingareaphone: str
    loadingareaaddress1: str
    loadingareaaddress2: str
    workingareacode: str
    workingareaname: str
    workingareaphone: str
    workingareaaddress1: str
    workingareaaddress2: str
    carryinareacode: str
    carryinareaname: str
    carryinareaphone: str
    carryinareaaddress1: str
    carryinareaaddress2: str
    remark: str
    destinataioncode: str
    destinataionname: str
    createuser: str
    updateuser: str
    create_at: str
    update_at: str

    def __init__(self,
                 id: str,
                 slipcode: str,
                 customercode: str,
                 customername: str,
                 salesofficecode: str,
                 salesofficename: str,
                 loadingdate: datetime,
                 carryindate: datetime,
                 billingdate: datetime,
                 loadingareacode: str,
                 loadingareaname: str,
                 loadingareaphone: str,
                 loadingareaaddress1: str,
                 loadingareaaddress2: str,
                 workingareacode: str,
                 workingareaname: str,
                 workingareaphone: str,
                 workingareaaddress1: str,
                 workingareaaddress2: str,
                 carryinareacode: str,
                 carryinareaname: str,
                 carryinareaphone: str,
                 carryinareaaddress1: str,
                 carryinareaaddress2: str,
                 remark: str,
                 destinataioncode: str,
                 destinataionname: str,
                 createuser: str,
                 updateuser: str,
                 create_at: datetime,
                 update_at: datetime):
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
