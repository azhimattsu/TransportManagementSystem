from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql.functions import current_timestamp
from tms.common.domain.valueobjects.common.cdatetime import CDateTime
from tms.master.infrastructure.mysql.mysql_setting import Base
from tms.master.domain.entities.container import ContainerEntity
from tms.master.domain.valueobjects import container


class Containers(Base):
    __tablename__ = "containers"
    id = Column(String(64), primary_key=True, nullable=False)
    code = Column(String(11), nullable=False)
    type = Column(Integer, nullable=False)
    tw = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    damage = Column(Integer, nullable=False)
    createuser = Column(String(60))
    updateuser = Column(String(60))
    create_at = Column(DateTime, server_default=current_timestamp())
    update_at = Column(DateTime, server_default=current_timestamp())


def fromEntity(entity: ContainerEntity) -> Containers:
    target = Containers()
    target.id = entity.id.value
    target.code = entity.code.value
    target.type = int(entity.type)
    target.tw = entity.tw.value
    target.height = int(entity.height)
    target.size = entity.size.value
    target.damage = entity.damage.value
    target.createuser = entity.createuser.value
    target.updateuser = entity.updateuser.value
    return target


def toEntity(row: Containers) -> ContainerEntity:
    target = ContainerEntity(container.Id(row.id),
                             container.Code(row.code),
                             container.Type(row.type),
                             container.TareWeight(row.tw),
                             container.Height(row.height),
                             container.Size(row.size),
                             container.Damage(row.damage),
                             container.MailAddress(row.createuser),
                             container.MailAddress(row.updateuser),
                             CDateTime(row.create_at),
                             CDateTime(row.update_at))
    return target
