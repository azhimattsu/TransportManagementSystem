from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, eq=True)
class ContainerData:
    container_id: str
    container_code: str
    type: int
    tw: int
    height: int
    size: int
    damage: int
    create_user: str
    update_user: str
    create_at: str
    update_at: str

    def __init__(self,
                 container_id: str,
                 container_code: str,
                 type: int,
                 tw: int,
                 height: int,
                 size: int,
                 damage: int,
                 create_user: str,
                 update_user: str,
                 create_at: datetime,
                 update_at: datetime):
        self.container_id = container_id
        self.container_code = container_code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
        self.create_user = create_user
        self.update_user = update_user
        self.create_at = create_at
        self.update_at = update_at
