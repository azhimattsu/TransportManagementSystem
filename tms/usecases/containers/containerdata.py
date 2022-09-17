from dataclasses import dataclass


@dataclass(init=False, eq=True)
class ContainerData:
    code: str
    type: int
    tw: int
    height: int
    size: int
    damage: int

    def __init__(self,
                 code: str,
                 type: int,
                 tw: int,
                 height: int,
                 size: int,
                 damage: int):
        self.code = code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
