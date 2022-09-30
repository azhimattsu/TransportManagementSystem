from tms.domain.valueobjects import common
from tms.domain.services.create_orderinfo_service import CreateOrderInfoService
from tms.domain.valueobjects import order
from tms.domain.entities.orderinfo import OrderInfoEntity
from .orderinfodata import OrderInfoData


class OrderInfoDataDto:

    @staticmethod
    def fromEntity(orderinfo: OrderInfoEntity) -> OrderInfoData:
        model = OrderInfoData(orderinfo.id.value,
                              orderinfo.slipcode.value,
                              orderinfo.customercode.value,
                              orderinfo.customername.value,
                              orderinfo.salesofficecode.value,
                              orderinfo.salesofficename.value,
                              orderinfo.loadingdate.getStr(),
                              orderinfo.carryindate.getStr(),
                              orderinfo.billingdate.getStr(),
                              orderinfo.loadingareacode.value,
                              orderinfo.loadingareaname.value,
                              orderinfo.loadingareaphone.value,
                              orderinfo.loadingareaaddress1.value,
                              orderinfo.loadingareaaddress2.value,
                              orderinfo.workingareacode.value,
                              orderinfo.workingareaname.value,
                              orderinfo.workingareaphone.value,
                              orderinfo.workingareaaddress1.value,
                              orderinfo.workingareaaddress2.value,
                              orderinfo.carryinareacode.value,
                              orderinfo.carryinareaname.value,
                              orderinfo.carryinareaphone.value,
                              orderinfo.carryinareaaddress1.value,
                              orderinfo.carryinareaaddress2.value,
                              orderinfo.remark.value,
                              orderinfo.destinataioncode.value,
                              orderinfo.destinataionname.value,
                              orderinfo.createuser.value,
                              orderinfo.updateuser.value,
                              orderinfo.create_at.getStr(),
                              orderinfo.update_at.getStr())
        return model

    @staticmethod
    def toEntity(orderinfodata: OrderInfoData) -> OrderInfoEntity:
        entity = OrderInfoEntity(order.Id(orderinfodata.id),
                                 order.SlipCode(orderinfodata.slipcode),
                                 order.CustomerCode(orderinfodata.customercode),
                                 order.Name(orderinfodata.customername),
                                 order.SalesOfficeCode(orderinfodata.salesofficecode),
                                 order.Name(orderinfodata.salesofficename),
                                 common.CreateDateTime(orderinfodata.loadingdate),
                                 common.CreateDateTime(orderinfodata.carryindate),
                                 common.CreateDateTime(orderinfodata.billingdate),
                                 order.LoadingAreaCode(orderinfodata.loadingareacode),
                                 order.Name(orderinfodata.loadingareaname),
                                 order.PhoneNumber(orderinfodata.loadingareaphone),
                                 order.Address(orderinfodata.loadingareaaddress1),
                                 order.Address(orderinfodata.loadingareaaddress2),
                                 order.WorkingAreaCode(orderinfodata.workingareacode),
                                 order.Name(orderinfodata.workingareaname),
                                 order.PhoneNumber(orderinfodata.workingareaphone),
                                 order.Address(orderinfodata.workingareaaddress1),
                                 order.Address(orderinfodata.workingareaaddress2),
                                 order.CarryInAreaCode(orderinfodata.carryinareacode),
                                 order.Name(orderinfodata.carryinareaname),
                                 order.PhoneNumber(orderinfodata.carryinareaphone),
                                 order.Address(orderinfodata.carryinareaaddress1),
                                 order.Address(orderinfodata.carryinareaaddress2),
                                 order.Remark(orderinfodata.remark),
                                 order.DestinationCode(orderinfodata.destinataioncode),
                                 order.Name(orderinfodata.destinataionname),
                                 common.MailAddress(orderinfodata.createuser),
                                 common.MailAddress(orderinfodata.updateuser),
                                 common.CreateDateTime(orderinfodata.create_at),
                                 common.CreateDateTime(orderinfodata.update_at))

        return entity

    @staticmethod
    def CreateEntity(orderinfodata: OrderInfoData) -> OrderInfoEntity:
        entity = OrderInfoEntity(CreateOrderInfoService.GetOrderInfoId(),
                                 order.SlipCode(orderinfodata.slipcode),
                                 order.CustomerCode(orderinfodata.customercode),
                                 order.Name(orderinfodata.customername),
                                 order.SalesOfficeCode(orderinfodata.salesofficecode),
                                 order.Name(orderinfodata.salesofficename),
                                 common.CreateDateTime(orderinfodata.loadingdate),
                                 common.CreateDateTime(orderinfodata.carryindate),
                                 common.CreateDateTime(orderinfodata.billingdate),
                                 order.LoadingAreaCode(orderinfodata.loadingareacode),
                                 order.Name(orderinfodata.loadingareaname),
                                 order.PhoneNumber(orderinfodata.loadingareaphone),
                                 order.Address(orderinfodata.loadingareaaddress1),
                                 order.Address(orderinfodata.loadingareaaddress2),
                                 order.WorkingAreaCode(orderinfodata.workingareacode),
                                 order.Name(orderinfodata.workingareaname),
                                 order.PhoneNumber(orderinfodata.workingareaphone),
                                 order.Address(orderinfodata.workingareaaddress1),
                                 order.Address(orderinfodata.workingareaaddress2),
                                 order.CarryInAreaCode(orderinfodata.carryinareacode),
                                 order.Name(orderinfodata.carryinareaname),
                                 order.PhoneNumber(orderinfodata.carryinareaphone),
                                 order.Address(orderinfodata.carryinareaaddress1),
                                 order.Address(orderinfodata.carryinareaaddress2),
                                 order.Remark(orderinfodata.remark),
                                 order.DestinationCode(orderinfodata.destinataioncode),
                                 order.Name(orderinfodata.destinataionname),
                                 common.MailAddress(orderinfodata.createuser),
                                 common.MailAddress(orderinfodata.updateuser),
                                 common.CreateDateTime(orderinfodata.create_at),
                                 common.CreateDateTime(orderinfodata.update_at))

        return entity
