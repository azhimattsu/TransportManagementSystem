from dataclasses import dataclass
from tms.domain.valueobjects import container


@dataclass(init=False, eq=True)
class ContainerParts:
    type: container.type
    tw: container.TareWeight
    height: container.Height
    size: container.Size
    damage: container.Damage

    def __init__(self,
                 type: container.Type,
                 tw: container.TareWeight,
                 height: container.Height,
                 size: container.Size,
                 damage: container.Damage):
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
