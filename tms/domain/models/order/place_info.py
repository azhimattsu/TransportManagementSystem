from dataclasses import dataclass

from tms.domain.models.order import PlaceCode
from tms.domain.models.order import PlaceName
from tms.domain.models.shared import PhoneNumber
from tms.domain.models.shared import Address


@dataclass(init=False, eq=True)
class PlaceInfo:
    code: PlaceCode = ""
    name: PlaceName = ""
    phone: PhoneNumber = ""
    address1: Address = ""
    address2: Address = ""

    def __init__(self, 
                 code: PlaceCode,
                 name: PlaceName,
                 phone: PhoneNumber,
                 address1: Address,
                 address2: Address):
        self.code = code
        self.name = name
        self.phone = phone
        self.address1 = address1
        self.address2 = address2
