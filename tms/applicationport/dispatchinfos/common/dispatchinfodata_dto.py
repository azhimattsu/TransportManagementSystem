from tms.domain.valueobjects import common, order
from tms.domain.services.create_container_service import CreateContainerService
from tms.domain.valueobjects import container
from tms.domain.valueobjects import dispatch
from tms.domain.entities.dispatchinfo import DispatchInfoEntity
from .dispatchinfodata import DispatchInfoData


class DispatchInfoDataDto:

    @staticmethod
    def from_entity(dispatchinfo: DispatchInfoEntity) -> DispatchInfoData:
        model = DispatchInfoData(dispatchinfo.container_id.value,
                                 dispatchinfo.day.getStr(),
                                 dispatchinfo.index,
                                 dispatchinfo.order_id.value,
                                 dispatchinfo.working_type,
                                 dispatchinfo.contractor_type,
                                 dispatchinfo.driver_code.value,
                                 dispatchinfo.vehicle_number.value,
                                 dispatchinfo.departure_point.value,
                                 dispatchinfo.arrival_point.value,
                                 dispatchinfo.sales,
                                 dispatchinfo.cost,
                                 dispatchinfo.remark.value,
                                 dispatchinfo.create_user.value,
                                 dispatchinfo.update_user.value,
                                 dispatchinfo.create_at.getStr(),
                                 dispatchinfo.update_at.getStr())
        return model

    @staticmethod
    def to_entity(dispatchinfodata: DispatchInfoData) -> DispatchInfoEntity:
        entity = DispatchInfoEntity(container.Id(dispatchinfodata.container_id),
                                    common.CreateDateTime(dispatchinfodata.day),
                                    dispatchinfodata.index,
                                    order.Id(dispatchinfodata.order_id),
                                    dispatchinfodata.working_type,
                                    dispatchinfodata.contractor_type,
                                    dispatch.DriverCode(dispatchinfodata.driver_code),
                                    dispatch.VehicleNumber(dispatchinfodata.vehicle_number),
                                    dispatch.PointCode(dispatchinfodata.departure_point),
                                    dispatch.PointCode(dispatchinfodata.arrival_point),
                                    dispatchinfodata.sales,
                                    dispatchinfodata.cost,
                                    dispatch.Remark(dispatchinfodata.remark),
                                    common.MailAddress(dispatchinfodata.create_user),
                                    common.MailAddress(dispatchinfodata.update_user),
                                    common.CreateDateTime(dispatchinfodata.create_at),
                                    common.CreateDateTime(dispatchinfodata.update_at))

        return entity

    @staticmethod
    def CreateEntity(dispatchinfodata: DispatchInfoData) -> DispatchInfoEntity:
        entity = DispatchInfoEntity(container.Id(dispatchinfodata.container_id),
                                    common.CreateDateTime(dispatchinfodata.day),
                                    dispatchinfodata.index,
                                    order.Id(dispatchinfodata.order_id),
                                    dispatchinfodata.working_type,
                                    dispatchinfodata.contractor_type,
                                    dispatch.DriverCode(dispatchinfodata.driver_code),
                                    dispatch.VehicleNumber(dispatchinfodata.vehicle_number),
                                    dispatch.PointCode(dispatchinfodata.departure_point),
                                    dispatch.PointCode(dispatchinfodata.arrival_point),
                                    dispatchinfodata.sales,
                                    dispatchinfodata.cost,
                                    dispatch.Remark(dispatchinfodata.remark),
                                    common.MailAddress(dispatchinfodata.create_user),
                                    common.MailAddress(dispatchinfodata.update_user),
                                    common.CreateDateTime(dispatchinfodata.create_at),
                                    common.CreateDateTime(dispatchinfodata.update_at))
        return entity
