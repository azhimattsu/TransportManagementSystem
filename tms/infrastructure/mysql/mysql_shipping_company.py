from typing import Optional

from tms.domain.models import shipping_company
import tms.infrastructure.mysql.datamodels.shipping_company_datamodel as oc
import tms.infrastructure.mysql.mysql_setting as s


class MySqlShippingCompany(shipping_company.ShippingCompanyRepository):

    def __init__(self):
        pass

    def fetch_all_data(self) -> list[shipping_company.ShippingCompanyInfo]:
        results: list[shipping_company.ShippingCompanyInfo] = []
        results.clear()

        rows = s.session.query(oc.ShippingCompanyDataModel).all()
        for row in rows:
            results.append(oc.to_entity(row))

        return results

    def find_data_bycode(self,
                         code: shipping_company.shipping_company_code) -> Optional[shipping_company.ShippingCompanyInfo]:
        row = s.session.query(oc.ShippingCompanyDataModel).filter(oc.ShippingCompanyDataModel.shipping_company_code == code.value).first()
        if row is None:
            return None

        return oc.to_entity(row)

    def find_data_byid(self, id: shipping_company.ShippingCompanyId) -> Optional[shipping_company.ShippingCompanyInfo]:
        row = s.session.query(oc.ShippingCompanyDataModel).filter(oc.ShippingCompanyDataModel.shipping_company_id == id.value).first()
        if row is None:
            return None

    def create_data(self, shipping_company: shipping_company.ShippingCompanyInfo):
        s.session.begin()
        row = oc.from_entity(shipping_company)
        s.session.add(row)
        s.session.commit()

    def update_data(self, shipping_company: shipping_company.ShippingCompanyInfo):
        s.session.begin()
        found = s.session.query(oc.ShippingCompanyDataModel).filter(oc.ShippingCompanyDataModel.shipping_company_id == shipping_company.shipping_company_id.value).first()
        if found is None:
            return

        found.import_entity(shipping_company)
        s.session.commit()
