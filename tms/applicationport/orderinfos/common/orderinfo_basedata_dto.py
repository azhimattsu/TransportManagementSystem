from tms.domain.valueobjects import common
from tms.domain.services.create_orderinfo_service import CreateOrderInfoService
from tms.domain.valueobjects import order
from tms.domain.entities.orderinfo_base import OrderInfoBaseEntity
from .orderinfo_basedata import OrderInfoBaseData


class OrderInfoBaseDataDto:

    @staticmethod
    def from_entity(orderinfo: OrderInfoBaseEntity) -> OrderInfoBaseData:
        model = OrderInfoBaseData(orderinfo.order_id.value,
                                  orderinfo.slip_code.value,
                                  orderinfo.customer_code.value,
                                  orderinfo.customer_name.value,
                                  orderinfo.salesoffice_code.value,
                                  orderinfo.salesoffice_name.value,
                                  orderinfo.loading_date.getStr(),
                                  orderinfo.carryin_date.getStr(),
                                  orderinfo.billing_date.getStr(),
                                  orderinfo.loading_area_code.value,
                                  orderinfo.loading_area_name.value,
                                  orderinfo.loading_area_phone.value,
                                  orderinfo.loading_area_address1.value,
                                  orderinfo.loading_area_address2.value,
                                  orderinfo.working_area_code.value,
                                  orderinfo.working_area_name.value,
                                  orderinfo.working_area_phone.value,
                                  orderinfo.working_area_address1.value,
                                  orderinfo.working_area_address2.value,
                                  orderinfo.carryin_area_code.value,
                                  orderinfo.carryin_area_name.value,
                                  orderinfo.carryin_area_phone.value,
                                  orderinfo.carryin_area_address1.value,
                                  orderinfo.carryin_area_address2.value,
                                  orderinfo.remark.value,
                                  orderinfo.destinataion_code.value,
                                  orderinfo.destinataion_name.value,
                                  orderinfo.create_user.value,
                                  orderinfo.update_user.value,
                                  orderinfo.create_at.getStr(),
                                  orderinfo.update_at.getStr())
        return model

    @staticmethod
    def to_entity(orderinfodata: OrderInfoBaseData) -> OrderInfoBaseEntity:
        entity = OrderInfoBaseEntity(order.Id(orderinfodata.order_id),
                                     order.SlipCode(orderinfodata.slip_code),
                                     order.CustomerCode(orderinfodata.customer_code),
                                     order.Name(orderinfodata.customer_name),
                                     order.SalesOfficeCode(orderinfodata.salesoffice_code),
                                     order.Name(orderinfodata.salesoffice_name),
                                     common.CreateDateTime(orderinfodata.loading_date),
                                     common.CreateDateTime(orderinfodata.carryin_date),
                                     common.CreateDateTime(orderinfodata.billing_date),
                                     order.LoadingAreaCode(orderinfodata.loading_area_code),
                                     order.Name(orderinfodata.loading_area_name),
                                     order.PhoneNumber(orderinfodata.loading_area_phone),
                                     order.Address(orderinfodata.loading_area_address1),
                                     order.Address(orderinfodata.loading_area_address2),
                                     order.WorkingAreaCode(orderinfodata.working_area_code),
                                     order.Name(orderinfodata.working_area_name),
                                     order.PhoneNumber(orderinfodata.working_area_phone),
                                     order.Address(orderinfodata.working_area_address1),
                                     order.Address(orderinfodata.working_area_address2),
                                     order.CarryInAreaCode(orderinfodata.carryin_area_code),
                                     order.Name(orderinfodata.carryin_area_name),
                                     order.PhoneNumber(orderinfodata.carryin_area_phone),
                                     order.Address(orderinfodata.carryin_area_address1),
                                     order.Address(orderinfodata.carryin_area_address2),
                                     order.Remark(orderinfodata.remark),
                                     order.DestinationCode(orderinfodata.destinataion_code),
                                     order.Name(orderinfodata.destinataion_name),
                                     common.MailAddress(orderinfodata.create_user),
                                     common.MailAddress(orderinfodata.update_user),
                                     common.CreateDateTime(orderinfodata.create_at),
                                     common.CreateDateTime(orderinfodata.update_at))

        return entity

    @staticmethod
    def CreateEntity(orderinfodata: OrderInfoBaseData) -> OrderInfoBaseEntity:
        entity = OrderInfoBaseEntity(CreateOrderInfoService.get_orderInfoid(),
                                     order.SlipCode(orderinfodata.slip_code),
                                     order.CustomerCode(orderinfodata.customer_code),
                                     order.Name(orderinfodata.customer_name),
                                     order.SalesOfficeCode(orderinfodata.salesoffice_code),
                                     order.Name(orderinfodata.salesoffice_name),
                                     common.CreateDateTime(orderinfodata.loading_date),
                                     common.CreateDateTime(orderinfodata.carryin_date),
                                     common.CreateDateTime(orderinfodata.billing_date),
                                     order.LoadingAreaCode(orderinfodata.loading_area_code),
                                     order.Name(orderinfodata.loading_area_name),
                                     order.PhoneNumber(orderinfodata.loading_area_phone),
                                     order.Address(orderinfodata.loading_area_address1),
                                     order.Address(orderinfodata.loading_area_address2),
                                     order.WorkingAreaCode(orderinfodata.working_area_code),
                                     order.Name(orderinfodata.working_area_name),
                                     order.PhoneNumber(orderinfodata.working_area_phone),
                                     order.Address(orderinfodata.working_area_address1),
                                     order.Address(orderinfodata.working_area_address2),
                                     order.CarryInAreaCode(orderinfodata.carryin_area_code),
                                     order.Name(orderinfodata.carryin_area_name),
                                     order.PhoneNumber(orderinfodata.carryin_area_phone),
                                     order.Address(orderinfodata.carryin_area_address1),
                                     order.Address(orderinfodata.carryin_area_address2),
                                     order.Remark(orderinfodata.remark),
                                     order.DestinationCode(orderinfodata.destinataion_code),
                                     order.Name(orderinfodata.destinataion_name),
                                     common.MailAddress(orderinfodata.create_user),
                                     common.MailAddress(orderinfodata.update_user),
                                     common.CreateDateTime(orderinfodata.create_at),
                                     common.CreateDateTime(orderinfodata.update_at))

        return entity
