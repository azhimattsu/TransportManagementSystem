from dataclasses import dataclass
from tms.domain.entities.container_parts import ContainerParts
from tms.domain.valueobjects import container
from tms.domain.valueobjects import common
from tms.domain.valueobjects import order


@dataclass(init=False, eq=True)
class OrderInfoContainerEntity(ContainerParts):
    order_id: order.Id
    index: int
    container_id: container.Id
    container_code: container.Code
    freight: int
    surcharge: int
    other: int
    create_user: common.MailAddress
    update_user: common.MailAddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 order_id: order.Id,
                 index: int,
                 container_id: container.Id,
                 container_code: container.Code,
                 type: container.Type,
                 tw: container.TareWeight,
                 height: container.Height,
                 size: container.Size,
                 damage: container.Damage,
                 freight: int,
                 surcharge: int,
                 other: int,
                 create_user: common.MailAddress,
                 update_user: common.MailAddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):
        super().__init__(type, tw, height, size, damage)
        self.order_id = order_id
        self.index = index
        self.container_id = container_id
        self.container_code = container_code
        self.freight = freight
        self.surcharge = surcharge
        self.other = other
        self.create_user = create_user
        self.update_user = update_user
        self.create_at = create_at
        self.update_at = update_at
