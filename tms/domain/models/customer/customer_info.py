from dataclasses import dataclass

from tms.domain.models.customer.customer_code import CustomerCode
from tms.domain.models.customer.customer_name import CustomerName


@dataclass(init=False, eq=True)
class CustomerInfo:
    code: CustomerCode = ""
    name: CustomerName = ""

    def __init__(self, code: CustomerCode, name: CustomerName):
        self.code = code
        self.name = name