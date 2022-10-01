from tms.domain.valueobjects import common
from tms.domain.services.create_orderinfo_service import CreateOrderInfoService
from tms.domain.valueobjects import container
from tms.domain.valueobjects import dispatch
from tms.domain.entities.dispatchinfo import DispatchInfoEntity
from .dispatchinfodata import DispatchInfoData


class DispatchInfoDataDto:

    @staticmethod
    def fromEntity(dispatchinfo: DispatchInfoEntity) -> DispatchInfoData:
        model = DispatchInfoData(dispatchinfo.containerId.value,
                                 dispatchinfo.day.getStr(),
                                 dispatchinfo.index,
                                 dispatchinfo.workingtype,
                                 dispatchinfo.contractortype,
                                 dispatchinfo.drivercode.value,
                                 dispatchinfo.vehiclenumber.value,
                                 dispatchinfo.departurepoint.value,
                                 dispatchinfo.arrivalpoint.value,
                                 dispatchinfo.sales,
                                 dispatchinfo.cost,
                                 dispatchinfo.remark.value,
                                 dispatchinfo.createuser.value,
                                 dispatchinfo.updateuser.value,
                                 dispatchinfo.create_at.getStr(),
                                 dispatchinfo.update_at.getStr())
        return model

    @staticmethod
    def toEntity(dispatchinfodata: DispatchInfoData) -> DispatchInfoEntity:
        entity = DispatchInfoEntity(container.Id(dispatchinfodata.containerId),
                                    common.CreateDateTime(dispatchinfodata.day),
                                    dispatchinfodata.index,
                                    dispatchinfodata.workingtype,
                                    dispatchinfodata.contractortype,
                                    dispatch.DriverCode(dispatchinfodata.drivercode),
                                    dispatch.VehicleNumber(dispatchinfodata.vehiclenumber),
                                    dispatch.PointCode(dispatchinfodata.departurepoint),
                                    dispatch.PointCode(dispatchinfodata.arrivalpoint),
                                    dispatchinfodata.sales,
                                    dispatchinfodata.cost,
                                    dispatch.Remark(dispatchinfodata.remark),
                                    common.MailAddress(dispatchinfodata.createuser),
                                    common.MailAddress(dispatchinfodata.updateuser),
                                    common.CreateDateTime(dispatchinfodata.create_at),
                                    common.CreateDateTime(dispatchinfodata.update_at))

        return entity

    @staticmethod
    def CreateEntity(dispatchinfodata: DispatchInfoData) -> DispatchInfoEntity:
        entity = DispatchInfoEntity(CreateOrderInfoService.GetOrderInfoId(),
                                    common.CreateDateTime(dispatchinfodata.day),
                                    dispatchinfodata.index,
                                    dispatchinfodata.workingtype,
                                    dispatchinfodata.contractortype,
                                    dispatch.DriverCode(dispatchinfodata.drivercode),
                                    dispatch.VehicleNumber(dispatchinfodata.vehiclenumber),
                                    dispatch.PointCode(dispatchinfodata.departurepoint),
                                    dispatch.PointCode(dispatchinfodata.arrivalpoint),
                                    dispatchinfodata.sales,
                                    dispatchinfodata.cost,
                                    dispatch.Remark(dispatchinfodata.remark),
                                    common.MailAddress(dispatchinfodata.createuser),
                                    common.MailAddress(dispatchinfodata.updateuser),
                                    common.CreateDateTime(dispatchinfodata.create_at),
                                    common.CreateDateTime(dispatchinfodata.update_at))

        return entity
