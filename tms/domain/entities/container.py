from dataclasses import dataclass

from ...domain.valueobjects.containerdamage import ContainerDamage
from ...domain.valueobjects.containercode import ContainerCode
from ...domain.valueobjects.containerheight import ContainerHeight
from ...domain.valueobjects.containersize import ContainerSize
from ...domain.valueobjects.containertype import ContainerType
from ...domain.valueobjects.tareweight import TareWeight


@dataclass(init=False, eq=True)
class Container:
    code: ContainerCode
    type: ContainerType
    tw: TareWeight
    height: ContainerHeight
    size: ContainerSize
    damage: ContainerDamage

    def __init__(self,
                 code: ContainerCode,
                 type: ContainerType,
                 tw: TareWeight,
                 height: ContainerHeight,
                 size: ContainerSize,
                 damage: ContainerDamage):
        self.code = code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
