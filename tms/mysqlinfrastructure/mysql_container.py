from typing import Optional

from tms.domain.valueobjects import container
from tms.domain.entities.container import ContainerEntity
from tms.domain.repositories.container_repository import ContainersRepository

import tms.mysqlinfrastructure.schemas.container as c
import tms.mysqlinfrastructure.mysql_setting as s


class MySqlContainers(ContainersRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[ContainerEntity]:
        results: list[ContainerEntity] = []
        results.clear()

        rows = s.session.query(c.Containers).all()
        for row in rows:
            results.append(c.toEntity(row))

        return results

    def find_data_bycode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        row = s.session.query(c.Containers).filter(c.Containers.code == code.value).first()
        if row is None:
            return None

        return c.toEntity(row)

    def find_data_byid(self, id: container.id) -> Optional[ContainerEntity]:
        row = s.session.query(c.Containers).filter(c.Containers.id == id.value).first()
        if row is None:
            return None

    def create_data(self, container: ContainerEntity):
        s.session.begin()
        row = c.fromEntity(container)
        s.session.add(row)
        s.session.commit()

    def update_data(self, container: ContainerEntity):
        s.session.begin()
        found = s.session.query(c.Containers).filter(c.Containers.id == container.id.value).first()
        if found is None:
            return

        found.importEntity(container)
        s.session.commit()
