from dataclasses import dataclass

from tms.domain.models import shared
from tms.domain.models import shipping_company


@dataclass(init=False, eq=True)
class ShippingCompanyInfo():
    shipping_company_id: shipping_company.ShippingCompanyId
    shipping_company_code: shipping_company.ShippingCompanyCode
    shipping_company_name: shipping_company.ShippingCompanyName
    update_info: shared.UpdateInfo

    def __init__(self,
                 shipping_company_id: shipping_company.ShippingCompanyId,
                 shipping_company_code: shipping_company.ShippingCompanyCode,
                 shipping_company_name: shipping_company.ShippingCompanyName,
                 update_info: shared.UpdateInfo):
        self.shipping_company_id = shipping_company_id
        self.shipping_company_code = shipping_company_code
        self.shipping_company_name = shipping_company_name
        self.update_info = update_info
