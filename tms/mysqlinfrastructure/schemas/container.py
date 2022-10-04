from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp
from tms.domain.valueobjects import common
from tms.mysqlinfrastructure.mysql_setting import Base
from tms.domain.entities.container import ContainerEntity
from tms.domain.valueobjects import container


class Containers(Base):
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

    def import_entity(self, entity: ContainerEntity):
        self.container_id = entity.container_id.value
        self.container_code = entity.container_code.value
        self.type = int(entity.type)
        self.tw = entity.tw.value
        self.height = int(entity.height)
        self.size = entity.size.value
        self.damage = entity.damage.value
        self.create_user = entity.create_user.value
        self.update_user = entity.update_user.value


def from_entity(entity: ContainerEntity) -> Containers:
    target = Containers()
    target.container_id = entity.container_id.value
    target.container_code = entity.container_code.value
    target.type = int(entity.type)
    target.tw = entity.tw.value
    target.height = int(entity.height)
    target.size = entity.size.value
    target.damage = entity.damage.value
    target.create_user = entity.create_user.value
    target.update_user = entity.update_user.value
    return target


def to_entity(row: Containers) -> ContainerEntity:
    target = ContainerEntity(container.Id(row.container_id),
                             container.Code(row.container_code),
                             container.Type(row.type),
                             container.TareWeight(row.tw),
                             container.Height(row.height),
                             container.Size(row.size),
                             container.Damage(row.damage),
                             common.MailAddress(row.create_user),
                             common.MailAddress(row.update_user),
                             common.CDateTime(row.create_at),
                             common.CDateTime(row.update_at))
    return target
