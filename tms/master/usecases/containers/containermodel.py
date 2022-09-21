from dataclasses import dataclass


@dataclass(init=False, eq=True)
class ContainerModel:
    id: str
    code: str
    type: int
    tw: int
    height: int
    size: int
    damage: int

    def __init__(self,
                 id: str,
                 code: str,
                 type: int,
                 tw: int,
                 height: int,
                 size: int,
                 damage: int):
        self.id = id
        self.code = code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
