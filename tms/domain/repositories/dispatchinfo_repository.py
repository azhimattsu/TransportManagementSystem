from abc import ABCMeta
from abc import abstractclassmethod

from tms.domain.valueobjects import common, container
from tms.domain.entities.dispatchinfo import DispatchInfoEntity


class DispatchInfosRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[DispatchInfoEntity]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: container.Id, day: common.CDateTime) -> list[DispatchInfoEntity]:
        pass

    @abstractclassmethod
    def create_data(self, dispatchinfo: DispatchInfoEntity):
        pass

    @abstractclassmethod
    def update_data(self, dispatchinfo: DispatchInfoEntity):
        pass
