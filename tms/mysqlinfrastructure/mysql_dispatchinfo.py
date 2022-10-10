from sqlalchemy import and_
from tms.domain.valueobjects import common, container
from tms.domain.entities.dispatchinfo import DispatchInfoEntity
from tms.domain.repositories.dispatchinfo_repository import DispatchInfosRepository

import tms.mysqlinfrastructure.schemas.dispatchinfo as c
import tms.mysqlinfrastructure.mysql_setting as s


class MySqlDispatchInfos(DispatchInfosRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[DispatchInfoEntity]:
        results: list[DispatchInfoEntity] = []
        results.clear()

        rows = s.session.query(c.DispatchInfo).all()
        for row in rows:
            results.append(c.to_entity(row))

        return results

    def find_data_byid(self, id: container.Id, day: common.CDateTime) -> list[DispatchInfoEntity]:
        results: list[DispatchInfoEntity] = []
        results.clear()

        rows = s.session.query(c.DispatchInfo).filter(and_(c.DispatchInfo.container_id == id.value, c.DispatchInfo.day == day)).all()

        for row in rows:
            results.append(c.to_entity(row))

        return results

    def create_data(self, dispatchinfo: DispatchInfoEntity):
        s.session.begin()
        row = c.from_entity(dispatchinfo)
        s.session.add(row)
        s.session.commit()

    def update_data(self, dispatchinfo: DispatchInfoEntity):
        s.session.begin()
        found = s.session.query(c.DispatchInfo).filter(and_(c.DispatchInfo.container_id == dispatchinfo.container_id.value,
                                                            c.DispatchInfo.day == dispatchinfo.day.value,
                                                            c.DispatchInfo.sort_id == dispatchinfo.sort_id)).first()
        if found is None:
            return

        found.import_entity(dispatchinfo)
        s.session.commit()
