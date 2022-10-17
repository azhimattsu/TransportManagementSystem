from dataclasses import dataclass
from tms.domain.models import shared
from tms.domain.models import order
from tms.domain.models import customer
from tms.domain.models import salesoffice
from tms.domain.models import distinations


@dataclass(init=False, eq=True)
class OrderDetail:
    order_id: order.OrderId
    slip_code: order.SlipCode
    customer_info: customer.CustomerInfo
    salesoffice_info: salesoffice.SalesOfficeInfo
    loading_date: shared.CDateTime
    carryin_date: shared.CDateTime
    billing_date: shared.CDateTime
    loading_area_info: order.PlaceInfo
    working_area_info: order.PlaceInfo
    carryin_area_info: order.PlaceInfo
    remark: shared.Remark
    destinataion_info: distinations.DistinationInfo
    update_info: shared.UpdateInfo

    def __init__(self,
                 order_id: order.OrderId,
                 slip_code: order.SlipCode,
                 customer_info: customer.CustomerInfo,
                 salesoffice_info: salesoffice.SalesOfficeInfo,
                 loading_date: shared.CDateTime,
                 carryin_date: shared.CDateTime,
                 billing_date: shared.CDateTime,
                 loading_area_info: order.PlaceInfo,
                 working_area_info: order.PlaceInfo,
                 carryin_area_info: order.PlaceInfo,
                 remark: shared.Remark,
                 destinataion_info: distinations.DistinationInfo,
                 update_info: shared.UpdateInfo):
        self.order_id = order_id
        self.slip_code = slip_code
        self.customer_info = customer_info
        self.salesoffice_info = salesoffice_info
        self.loading_date = loading_date
        self.carryin_date = carryin_date
        self.billing_date = billing_date
        self.loading_area_info = loading_area_info
        self.working_area_info = working_area_info
        self.carryin_area_info = carryin_area_info
        self.remark = remark
        self.destinataion_info = destinataion_info
        self.update_info = update_info
