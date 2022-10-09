from dataclasses import dataclass
from datetime import datetime


@dataclass(init=False, eq=True)
class OrderInfoBaseData:
    order_id: str
    slip_code: str
    customer_code: str
    customer_name: str
    salesoffice_code: str
    salesoffice_name: str
    loading_date: str
    carryin_date: str
    billing_date: str
    loading_area_code: str
    loading_area_name: str
    loading_area_phone: str
    loading_area_address1: str
    loading_area_address2: str
    working_area_code: str
    working_area_name: str
    working_area_phone: str
    working_area_address1: str
    working_area_address2: str
    carryin_area_code: str
    carryin_area_name: str
    carryin_area_phone: str
    carryin_area_address1: str
    carryin_area_address2: str
    remark: str
    destinataion_code: str
    destinataion_name: str
    create_user: str
    update_user: str
    create_at: str
    update_at: str

    def __init__(self,
                 order_id: str,
                 slip_code: str,
                 customer_code: str,
                 customer_name: str,
                 salesoffice_code: str,
                 salesoffice_name: str,
                 loading_date: datetime,
                 carryin_date: datetime,
                 billing_date: datetime,
                 loading_area_code: str,
                 loading_area_name: str,
                 loading_area_phone: str,
                 loading_area_address1: str,
                 loading_area_address2: str,
                 working_area_code: str,
                 working_area_name: str,
                 working_area_phone: str,
                 working_area_address1: str,
                 working_area_address2: str,
                 carryin_area_code: str,
                 carryin_area_name: str,
                 carryin_area_phone: str,
                 carryin_area_address1: str,
                 carryin_area_address2: str,
                 remark: str,
                 destinataion_code: str,
                 destinataion_name: str,
                 create_user: str,
                 update_user: str,
                 create_at: datetime,
                 update_at: datetime):
        self.order_id = order_id
        self.slip_code = slip_code
        self.customer_code = customer_code
        self.customer_name = customer_name
        self.salesoffice_code = salesoffice_code
        self.salesoffice_name = salesoffice_name
        self.loading_date = loading_date
        self.carryin_date = carryin_date
        self.billing_date = billing_date
        self.loading_area_code = loading_area_code
        self.loading_area_name = loading_area_name
        self.loading_area_phone = loading_area_phone
        self.loading_area_address1 = loading_area_address1
        self.loading_area_address2 = loading_area_address2
        self.working_area_code = working_area_code
        self.working_area_name = working_area_name
        self.working_area_phone = working_area_phone
        self.working_area_address1 = working_area_address1
        self.working_area_address2 = working_area_address2
        self.carryin_area_code = carryin_area_code
        self.carryin_area_name = carryin_area_name
        self.carryin_area_phone = carryin_area_phone
        self.carryin_area_address1 = carryin_area_address1
        self.carryin_area_address2 = carryin_area_address2
        self.remark = remark
        self.destinataion_code = destinataion_code
        self.destinataion_name = destinataion_name
        self.create_user = create_user
        self.update_user = update_user
        self.create_at = create_at
        self.update_at = update_at
