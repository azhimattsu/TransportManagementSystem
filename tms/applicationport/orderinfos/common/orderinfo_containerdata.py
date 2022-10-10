from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, eq=True)
class OrderInfoContainerData:
    order_id: str
    sort_id: int
    container_id: str
    container_code: str
    type: int
    tw: int
    height: int
    size: int
    damage: int
    freight: int
    surcharge: int
    other: int
    create_user: str
    update_user: str
    create_at: datetime
    update_at: datetime

    def __init__(self,
                 order_id: str,
                 sort_id: int,
                 container_id: str,
                 container_code: str,
                 type: int,
                 tw: int,
                 height: int,
                 size: int,
                 damage: int,
                 freight: int,
                 surcharge: int,
                 other: int,
                 create_user: str,
                 update_user: str,
                 create_at: datetime,
                 update_at: datetime):
        self.order_id = order_id
        self.sort_id = sort_id
        self.container_id = container_id
        self.container_code = container_code
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
        self.freight = freight
        self.surcharge = surcharge
        self.other = other
        self.create_user = create_user
        self.update_user = update_user
        self.create_at = create_at
        self.update_at = update_at

