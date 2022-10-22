from typing import Optional

from tms.domain.models import chassis
import tms.infrastructure.mysql.datamodels.chassis_datamodel as oc
import tms.infrastructure.mysql.mysql_setting as s


class MySqlChassis(chassis.ChassisRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[chassis.ChassisInfo]:
        results: list[chassis.ChassisInfo] = []
        results.clear()

        rows = s.session.query(oc.ChassisDataModel).all()
        for row in rows:
            results.append(oc.to_entity(row))

        return results

    def find_data_bycode(self,
                         code: chassis.ChassisCode) -> Optional[chassis.ChassisInfo]:
        row = s.session.query(oc.ChassisDataModel).filter(oc.ChassisDataModel.chassis_code == code.value).first()
        if row is None:
            return None

        return oc.to_entity(row)

    def find_data_byid(self, id: chassis.ChassisId) -> Optional[chassis.ChassisInfo]:
        row = s.session.query(oc.ChassisDataModel).filter(oc.ChassisDataModel.chassis_id == id.value).first()
        if row is None:
            return None

    def create_data(self, chassis: chassis.ChassisInfo):
        s.session.begin()
        row = oc.from_entity(chassis)
        s.session.add(row)
        s.session.commit()

    def update_data(self, chassis: chassis.ChassisInfo):
        s.session.begin()
        found = s.session.query(oc.ChassisDataModel).filter(oc.ChassisDataModel.chassis_id == chassis.chassis_id.value).first()
        if found is None:
            return

        found.import_entity(chassis)
        s.session.commit()
