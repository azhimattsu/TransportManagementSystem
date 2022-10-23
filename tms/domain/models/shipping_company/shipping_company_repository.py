from abc import ABCMeta
from abc import abstractclassmethod
from typing import Optional

from tms.domain.models import shipping_company


class ShippingCompanyRepository(metaclass=ABCMeta):
    @abstractclassmethod
    def fetch_all_data(self) -> list[shipping_company.ShippingCompanyInfo]:
        pass

    @abstractclassmethod
    def find_data_bycode(self,
                         code: shipping_company.ShippingCompanyCode) -> Optional[shipping_company.ShippingCompanyInfo]:
        pass

    @abstractclassmethod
    def find_data_byid(self, id: shipping_company.ShippingCompanyId) -> Optional[shipping_company.ShippingCompanyInfo]:
        pass

    @abstractclassmethod
    def create_data(self, shipping_company: shipping_company.ShippingCompanyInfo):
        pass

    @abstractclassmethod
    def update_data(self, shipping_company: shipping_company.ShippingCompanyInfo):
        pass
