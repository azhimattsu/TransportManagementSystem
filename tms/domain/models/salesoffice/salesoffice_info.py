from dataclasses import dataclass

from tms.domain.models.salesoffice import SalesOfficeCode
from tms.domain.models.salesoffice import SalesOfficeName


@dataclass(init=False, eq=True)
class SalesOfficeInfo:
    code: SalesOfficeCode = ""
    name: SalesOfficeName = ""

    def __init__(self, code: SalesOfficeCode, name: SalesOfficeName):
        self.code = code
        self.name = name
