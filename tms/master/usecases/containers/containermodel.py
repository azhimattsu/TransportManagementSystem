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
    createuser: str
    updateuser: str

    def __init__(self,
                 id: str,
                 code: str,
                 type: int,
                 tw: int,
                 height: int,
                 size: int,
                 damage: int,
                 createuser: str,
                 updateuser: str):
        self.id = id
        self.code = code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
        self.createuser = createuser
        self.updateuser = updateuser
