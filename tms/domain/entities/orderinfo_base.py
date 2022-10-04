from dataclasses import dataclass

from tms.domain.valueobjects import common, order


@dataclass(init=False, eq=True)
class OrderInfoBaseEntity:
    order_id: order.Id
    slip_code: order.SlipCode
    customer_code: order.CustomerCode
    customer_name: order.Name
    salesoffice_code: order.SalesOfficeCode
    salesoffice_name: order.Name
    loading_date: common.CDateTime
    carryin_date: common.CDateTime
    billing_date: common.CDateTime
    loading_area_code: order.LoadingAreaCode
    loading_area_name: order.Name
    loading_area_phone: order.PhoneNumber
    loading_area_address1: order.Address
    loading_area_address2: order.Address
    working_area_code: order.WorkingAreaCode
    working_area_name: order.Name
    working_area_phone: order.PhoneNumber
    working_area_address1: order.Address
    working_area_address2: order.Address
    carryin_area_code: order.CarryInAreaCode
    carryin_area_name: order.Name
    carryin_area_phone: order.PhoneNumber
    carryin_area_address1: order.Address
    carryin_area_address2: order.Address
    remark: order.Remark
    destinataion_code: order.DestinationCode
    destinataion_name: order.Name
    create_user: common.MailAddress
    update_user: common.MailAddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 order_id: order.Id,
                 slip_code: order.SlipCode,
                 customer_code: order.CustomerCode,
                 customer_name: order.Name,
                 salesoffice_code: order.SalesOfficeCode,
                 salesoffice_name: order.Name,
                 loading_date: common.CDateTime,
                 carryin_date: common.CDateTime,
                 billing_date: common.CDateTime,
                 loading_area_code: order.LoadingAreaCode,
                 loading_area_name: order.Name,
                 loading_area_phone: order.PhoneNumber,
                 loading_area_address1: order.Address,
                 loading_area_address2: order.Address,
                 working_area_code: order.WorkingAreaCode,
                 working_area_name: order.Name,
                 working_area_phone: order.PhoneNumber,
                 working_area_address1: order.Address,
                 working_area_address2: order.Address,
                 carryin_area_code: order.CarryInAreaCode,
                 carryin_area_name: order.Name,
                 carryin_area_phone: order.PhoneNumber,
                 carryin_area_address1: order.Address,
                 carryin_area_address2: order.Address,
                 remark: order.Remark,
                 destinataion_code: order.DestinationCode,
                 destinataion_name: order.Name,
                 create_user: common.MailAddress,
                 update_user: common.MailAddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):
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
