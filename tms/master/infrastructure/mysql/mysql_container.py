from typing import Optional
from tms.common.domain.valueobjects.common.cdatetime import CDateTime

from tms.master.domain.valueobjects import container
from tms.master.domain.entities.container import ContainerEntity
from tms.master.domain.repositories.containers_repository import ContainersRepository

import tms.master.infrastructure.mysql.schemas.containers as c
import tms.master.infrastructure.mysql.mysql_setting as s


class MySqlContainers(ContainersRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[ContainerEntity]:
        results: list[ContainerEntity] = []
        results.clear()

        items = s.session.query(c.Containers).all()

        for item in items:
            containerItem = ContainerEntity(container.Id(item.id),
                                            container.Code(item.code),
                                            container.Type(item.type),
                                            container.TareWeight(item.tw),
                                            container.Height(item.height),
                                            container.Size(item.size),
                                            container.Damage(item.damage),
                                            container.MailAddress(item.createuser),
                                            container.MailAddress(item.updateuser),
                                            CDateTime(item.create_at),
                                            CDateTime(item.update_at))
            results.append(containerItem)
        return results

    def find_data_bycode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        item = s.session.query(c.Containers).filter(c.Containers.code == code.value).first()
        if item is None:
            return None

        containerItem = ContainerEntity(container.Id(item.id),
                                        container.Code(item.code),
                                        container.Type(item.type),
                                        container.TareWeight(item.tw),
                                        container.Height(item.height),
                                        container.Size(item.size),
                                        container.Damage(item.damage),
                                        container.MailAddress(item.createuser),
                                        container.MailAddress(item.updateuser),
                                        CDateTime(item.create_at),
                                        CDateTime(item.update_at))
        return containerItem

    def create_data(self, container: ContainerEntity):
        s.session.begin()
        target = c.Containers()
        target.id = container.id.value
        target.code = container.code.value
        target.type = int(container.type)
        target.tw = container.tw.value
        target.height = int(container.height)
        target.size = container.size.value
        target.damage = container.damage.value
        target.createuser = container.createuser.value
        target.updateuser = container.updateuser.value
        s.session.add(target)
        s.session.commit()
