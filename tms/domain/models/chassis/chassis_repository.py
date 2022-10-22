from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from tms.domain.models import chassis


class ChassisRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[chassis.ChassisInfo]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: chassis.ChassisCode) -> Optional[chassis.ChassisInfo]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: chassis.ChassisId) -> Optional[chassis.ChassisInfo]:
        pass

    @abstractclassmethod
    def create_data(self, chassis: chassis.ChassisInfo):
        pass

    @abstractclassmethod
    def update_data(self, chassis: chassis.ChassisInfo):
        pass
