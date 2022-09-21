from dataclasses import dataclass
from tms.master.domain.valueobjects import container


@dataclass(init=False, eq=True)
class ContainerEntity:
    code: container.Code
    type: container.TareWeight
    tw: container.TareWeight
    height: container.Height
    size: container.Size
    damage: container.Damage

    def __init__(self,
                 code: container.Code,
                 type: container.Type,
                 tw: container.TareWeight,
                 height: container.Height,
                 size: container.Size,
                 damage: container.Damage):
        self.code = code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
