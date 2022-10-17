
from tms.applicationport.order.shared.order_detail_data import OrderDetailData
from tms.domain.models.customer.customer_code import CustomerCode
from tms.domain.services.create_orderinfo_service import CreateOrderInfoService
from tms.domain.models import shared
from tms.domain.models import order
from tms.domain.models import customer
from tms.domain.models import salesoffice
from tms.domain.models import distinations


class OrderDetailDataDto:

    @staticmethod
    def from_entity(orderinfo: order.OrderDetail) -> OrderDetailData:
        model = OrderDetailData(orderinfo.order_id.value,
                                orderinfo.slip_code.value,
                                orderinfo.customer_info.code.value,
                                orderinfo.customer_info.name.value,
                                orderinfo.salesoffice_info.code.value,
                                orderinfo.salesoffice_info.name.value,
                                orderinfo.loading_date.getStr(),
                                orderinfo.carryin_date.getStr(),
                                orderinfo.billing_date.getStr(),
                                orderinfo.loading_area_info.code.value,
                                orderinfo.loading_area_info.name.value,
                                orderinfo.loading_area_info.phone.value,
                                orderinfo.loading_area_info.address1.value,
                                orderinfo.loading_area_info.address2.value,
                                orderinfo.working_area_info.code.value,
                                orderinfo.working_area_info.name.value,
                                orderinfo.working_area_info.phone.value,
                                orderinfo.working_area_info.address1.value,
                                orderinfo.working_area_info.address2.value,
                                orderinfo.carryin_area_info.code.value,
                                orderinfo.carryin_area_info.name.value,
                                orderinfo.carryin_area_info.phone.value,
                                orderinfo.carryin_area_info.address1.value,
                                orderinfo.carryin_area_info.address2.value,
                                orderinfo.remark.value,
                                orderinfo.destinataion_info.code.value,
                                orderinfo.destinataion_info.name.value,
                                orderinfo.update_info.create_user.value,
                                orderinfo.update_info.update_user.value,
                                orderinfo.update_info.create_at.getStr(),
                                orderinfo.update_info.update_at.getStr())
        return model

    @staticmethod
    def to_entity(orderinfodata: OrderDetailData) -> order.OrderDetail:
        entity = order.OrderDetail(order.OrderId(orderinfodata.order_id),
                                   order.SlipCode(orderinfodata.slip_code),
                                   customer.CustomerInfo(customer.CustomerCode(orderinfodata.customer_code),
                                                         customer.CustomerName(orderinfodata.customer_name)),
                                   salesoffice.SalesOfficeInfo(salesoffice.SalesOfficeCode(orderinfodata.salesoffice_code),
                                                               salesoffice.SalesOfficeName(orderinfodata.salesoffice_name)),
                                   shared.CDateTime(orderinfodata.loading_date),
                                   shared.CDateTime(orderinfodata.carryin_date),
                                   shared.CDateTime(orderinfodata.billing_date),
                                   order.PlaceInfo(order.PlaceCode(orderinfodata.loading_area_code),
                                                   order.PlaceName(orderinfodata.loading_area_name),
                                                   shared.PhoneNumber(orderinfodata.loading_area_phone),
                                                   shared.Address(orderinfodata.loading_area_address1),
                                                   shared.Address(orderinfodata.loading_area_address2)),
                                   order.PlaceInfo(order.PlaceCode(orderinfodata.working_area_code),
                                                   order.PlaceName(orderinfodata.working_area_name),
                                                   shared.PhoneNumber(orderinfodata.working_area_phone),
                                                   shared.Address(orderinfodata.working_area_address1),
                                                   shared.Address(orderinfodata.working_area_address2)),
                                   order.PlaceInfo(order.PlaceCode(orderinfodata.carryin_area_code),
                                                   order.PlaceName(orderinfodata.carryin_area_name),
                                                   shared.PhoneNumber(orderinfodata.carryin_area_phone),
                                                   shared.Address(orderinfodata.working_area_address1),
                                                   shared.Address(orderinfodata.carryin_area_address2)),
                                   shared.Remark(orderinfodata.remark),
                                   distinations.DistinationInfo(distinations.DistinationCode(orderinfodata.destinataion_code),
                                                                distinations.DistinationName(orderinfodata.destinataion_name)),
                                   shared.UpdateInfo(shared.MailAddress(orderinfodata.create_user),
                                                     shared.MailAddress(orderinfodata.update_user),
                                                     shared.CDateTime(orderinfodata.create_at),
                                                     shared.CDateTime(orderinfodata.update_at)))

        return entity

    @staticmethod
    def CreateEntity(orderinfodata: OrderDetailData) -> order.OrderDetail:
        entity = order.OrderDetail(CreateOrderInfoService.get_orderInfoid(),
                                   order.SlipCode(orderinfodata.slip_code),
                                   customer.CustomerInfo(customer.CustomerCode(orderinfodata.customer_code),
                                                         customer.CustomerName(orderinfodata.customer_name)),
                                   salesoffice.SalesOfficeInfo(salesoffice.SalesOfficeCode(orderinfodata.salesoffice_code),
                                                               salesoffice.SalesOfficeName(orderinfodata.salesoffice_name)),
                                   shared.CDateTime(orderinfodata.loading_date),
                                   shared.CDateTime(orderinfodata.carryin_date),
                                   shared.CDateTime(orderinfodata.billing_date),
                                   order.PlaceInfo(order.PlaceCode(orderinfodata.loading_area_code),
                                                   order.PlaceName(orderinfodata.loading_area_name),
                                                   shared.PhoneNumber(orderinfodata.loading_area_phone),
                                                   shared.Address(orderinfodata.loading_area_address1),
                                                   shared.Address(orderinfodata.loading_area_address2)),
                                   order.PlaceInfo(order.PlaceCode(orderinfodata.working_area_code),
                                                   order.PlaceName(orderinfodata.working_area_name),
                                                   shared.PhoneNumber(orderinfodata.working_area_phone),
                                                   shared.Address(orderinfodata.working_area_address1),
                                                   shared.Address(orderinfodata.working_area_address2)),
                                   order.PlaceInfo(order.PlaceCode(orderinfodata.carryin_area_code),
                                                   order.PlaceName(orderinfodata.carryin_area_name),
                                                   shared.PhoneNumber(orderinfodata.carryin_area_phone),
                                                   shared.Address(orderinfodata.working_area_address1),
                                                   shared.Address(orderinfodata.carryin_area_address2)),
                                   shared.Remark(orderinfodata.remark),
                                   distinations.DistinationInfo(distinations.DistinationCode(orderinfodata.destinataion_code),
                                                                distinations.DistinationName(orderinfodata.destinataion_name)),
                                   shared.UpdateInfo(shared.MailAddress(orderinfodata.create_user),
                                                     shared.MailAddress(orderinfodata.update_user),
                                                     shared.CDateTime(orderinfodata.create_at),
                                                     shared.CDateTime(orderinfodata.update_at)))
        return entity
