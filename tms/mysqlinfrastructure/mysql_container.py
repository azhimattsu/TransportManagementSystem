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
            results.append(c.to_entity(row))

        return results

    def find_data_bycode(self,
                         code: container.Code) -> Optional[ContainerEntity]:
        row = s.session.query(c.Containers).filter(c.Containers.container_code == code.value).first()
        if row is None:
            return None

        return c.to_entity(row)

    def find_data_byid(self, id: container.id) -> Optional[ContainerEntity]:
        row = s.session.query(c.Containers).filter(c.Containers.container_id == id.value).first()
        if row is None:
            return None

    def create_data(self, container: ContainerEntity):
        s.session.begin()
        row = c.from_entity(container)
        s.session.add(row)
        s.session.commit()

    def update_data(self, container: ContainerEntity):
        s.session.begin()
        found = s.session.query(c.Containers).filter(c.Containers.container_id == container.container_id.value).first()
        if found is None:
            return

        found.import_entity(container)
        s.session.commit()
