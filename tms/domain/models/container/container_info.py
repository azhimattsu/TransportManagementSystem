from dataclasses import dataclass

from tms.domain.models import shared
from tms.domain.models import container


@dataclass(init=False, eq=True)
class ContainerInfo():
    container_id: container.ContainerId
    container_code: container.ContainerCode
    type: container.type
    tw: container.TareWeight
    height: container.Height
    size: container.Size
    damage: container.Damage
    update_info: shared.UpdateInfo

    def __init__(self,
                 container_id: container.ContainerId,
                 container_code: container.ContainerCode,
                 type: container.Type,
                 tw: container.TareWeight,
                 height: container.Height,
                 size: container.Size,
                 damage: container.Damage,
                 update_info: shared.UpdateInfo):
        self.type = type
        self.tw = tw
        self.height = height
        self.size = size
        self.damage = damage
        self.container_id = container_id
        self.container_code = container_code
        self.update_info = update_info
