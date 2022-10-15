from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp

from tms.infrastructure.mysql.mysql_setting import Base

from tms.domain.models import container
from tms.domain.models import shared


class ContainerDataModel(Base):
    __tablename__ = "container"
    container_id = Column(String(64), primary_key=True, nullable=False)
    container_code = Column(String(11), nullable=False)
    type = Column(Integer, nullable=False)
    tw = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)
    create_user = Column(String(60))
    update_user = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())

    def import_entity(self, entity: container.ContainerInfo):
        self.container_id = entity.container_id.value
        self.container_code = entity.container_code.value
        self.type = int(entity.type)
        self.tw = entity.tw.value
        self.height = int(entity.height)
        self.size = entity.size.value
        self.damage = entity.damage.value
        self.create_user = entity.update_info.create_user.value
        self.update_user = entity.update_info.update_user.value


def from_entity(entity: container.ContainerInfo) -> ContainerDataModel:
    target = ContainerDataModel()
    target.import_entity(entity)
    return target


def to_entity(row: ContainerDataModel) -> container.ContainerInfo:
    target = container.ContainerInfo(container.ContainerId(row.container_id),
                                     container.ContainerCode(row.container_code),
                                     container.Type(row.type),
                                     container.TareWeight(row.tw),
                                     container.Height(row.height),
                                     container.Size(row.size),
                                     container.Damage(row.damage),
                                     shared.UpdateInfo(shared.MailAddress(row.create_user),
                                                       shared.MailAddress(row.update_user),
                                                       shared.CDateTime(row.create_at),
                                                       shared.CDateTime(row.update_at)))
    return target
