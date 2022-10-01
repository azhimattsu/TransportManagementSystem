from typing import Optional
from sqlalchemy import and_
from tms.domain.valueobjects import common, container
from tms.domain.entities.dispatchinfo import DispatchInfoEntity
from tms.domain.repositories.dispatchinfos_repository import DispatchInfosRepository

import tms.mysqlinfrastructure.schemas.dispatchinfos as c
import tms.mysqlinfrastructure.mysql_setting as s


class MySqlDispatchInfos(DispatchInfosRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[DispatchInfoEntity]:
        results: list[DispatchInfoEntity] = []
        results.clear()

        rows = s.session.query(c.DispatchInfos).all()
        for row in rows:
            results.append(c.toEntity(row))

        return results

    def find_data_byid(self, id: container.Id, day: common.CDateTime) -> list[DispatchInfoEntity]:
        results: list[DispatchInfoEntity] = []
        results.clear()

        rows = s.session.query(c.Containers).filter(and_(c.DispatchInfos.containerId == id.value, c.DispatchInfos.day == day)).all()

        for row in rows:
            results.append(c.toEntity(row))

        return results

    def create_data(self, dispatchinfo: DispatchInfoEntity):
        s.session.begin()
        row = c.fromEntity(container)
        s.session.add(row)
        s.session.commit()

    def update_data(self, dispatchinfo: DispatchInfoEntity):
        s.session.begin()
        found = s.session.query(c.Containers).filter(and_(c.DispatchInfos.containerId == dispatchinfo.containerId.value,
                                                          c.DispatchInfos.day == dispatchinfo.containerId.day,
                                                          c.DispatchInfos.index == dispatchinfo.index)).first()
        if found is None:
            return

        found.importEntity(container)
        s.session.commit()
