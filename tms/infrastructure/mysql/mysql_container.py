from typing import Optional

from tms.domain.models import container
import tms.infrastructure.mysql.datamodels.container_datamodel as oc
import tms.infrastructure.mysql.mysql_setting as s


class MySqlContainer(container.ContainerRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[container.ContainerInfo]:
        results: list[container.ContainerInfo] = []
        results.clear()

        rows = s.session.query(oc.ContainerDataModel).all()
        for row in rows:
            results.append(oc.to_entity(row))

        return results

    def find_data_bycode(self,
                         code: container.ContainerCode) -> Optional[container.ContainerInfo]:
        row = s.session.query(oc.ContainerDataModel).filter(oc.ContainerDataModel.container_code == code.value).first()
        if row is None:
            return None

        return oc.to_entity(row)

    def find_data_byid(self, id: container.ContainerId) -> Optional[container.ContainerInfo]:
        row = s.session.query(oc.ContainerDataModel).filter(oc.ContainerDataModel.container_id == id.value).first()
        if row is None:
            return None

    def create_data(self, container: container.ContainerInfo):
        s.session.begin()
        row = oc.from_entity(container)
        s.session.add(row)
        s.session.commit()

    def update_data(self, container: container.ContainerInfo):
        s.session.begin()
        found = s.session.query(oc.ContainerDataModel).filter(oc.ContainerDataModel.container_id == container.container_id.value).first()
        if found is None:
            return

        found.import_entity(container)
        s.session.commit()
