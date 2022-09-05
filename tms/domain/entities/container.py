from dataclasses import dataclass

from ...domain.valueobjects.containercode import ContainerCode
from ...domain.valueobjects.containerheight import ContainerHeight
from ...domain.valueobjects.containersize import ContainerSize
from ...domain.valueobjects.containertype import ContainerType
from ...domain.valueobjects.tareweight import TareWeight


@dataclass(init=False, eq=True, frozen=True)
class Container:
    code: ContainerCode
    type: ContainerType
    tw: TareWeight
    height: ContainerHeight
    size: ContainerSize

    def __init__(self,
                 code: ContainerCode,
                 type: ContainerType,
                 tw: TareWeight,
                 height: ContainerHeight,
                 size: ContainerSize):
        object.__setattr__(self, "code", code)
        object.__setattr__(self, "type", type)
        object.__setattr__(self, "tw", tw)
        object.__setattr__(self, "height", height)
        object.__setattr__(self, "size", size)
