from dataclasses import dataclass
from tms.master.domain.valueobjects import container
from tms.common.domain.valueobjects import common


@dataclass(init=False, eq=True)
class ContainerEntity:
    id: container.Id
    code: container.Code
    type: container.type
    tw: container.TareWeight
    height: container.Height
    size: container.Size
    damage: container.Damage
    createuser: container.mailaddress
    updateuser: container.mailaddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 id: container.Id,
                 code: container.Code,
                 type: container.Type,
                 tw: container.TareWeight,
                 height: container.Height,
                 size: container.Size,
                 damage: container.Damage,
                 createuser: container.mailaddress,
                 updateuser: container.mailaddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):
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
