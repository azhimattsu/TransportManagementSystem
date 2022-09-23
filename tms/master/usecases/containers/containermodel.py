from dataclasses import dataclass
from datetime import datetime


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
    create_at: str
    update_at: str

    def __init__(self,
                 id: str,
                 code: str,
                 type: int,
                 tw: int,
                 height: int,
                 size: int,
                 damage: int,
                 createuser: str,
                 updateuser: str,
                 create_at: datetime,
                 update_at: datetime):
        self.id = id
        self.code = code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
        self.createuser = createuser
        self.updateuser = updateuser
        self.create_at = create_at
        self.update_at = update_at
