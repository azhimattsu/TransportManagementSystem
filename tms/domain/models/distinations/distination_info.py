from dataclasses import dataclass

from tms.domain.models.distinations import DistinationCode
from tms.domain.models.distinations import DistinationName


@dataclass(init=False, eq=True)
class DistinationInfo:
    code: DistinationCode = ""
    name: DistinationName = ""

    def __init__(self, code: DistinationCode, name: DistinationName):
        self.code = code
        self.name = name
