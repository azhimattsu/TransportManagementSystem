from dataclasses import dataclass
from tms.domain.valueobjects import container
from tms.domain.valueobjects import common


@dataclass(init=False, eq=True)
class ContainerEntity:
    container_id: container.Id
    container_code: container.Code
    type: container.type
    tw: container.TareWeight
    height: container.Height
    size: container.Size
    damage: container.Damage
    create_user: common.MailAddress
    update_user: common.MailAddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 container_id: container.Id,
                 container_code: container.Code,
                 type: container.Type,
                 tw: container.TareWeight,
                 height: container.Height,
                 size: container.Size,
                 damage: container.Damage,
                 create_user: common.MailAddress,
                 update_user: common.MailAddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):
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
