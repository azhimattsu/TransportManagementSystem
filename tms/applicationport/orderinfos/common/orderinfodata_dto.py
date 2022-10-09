from tms.applicationport.orderinfos.common.orderinfo_basedata_dto import OrderInfoBaseDataDto
from tms.applicationport.orderinfos.common.orderinfo_containerdata_dto import OrderInfoContainerDataDto
from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData
from tms.domain.entities.orderinfo import OrderInfoEntity
from .orderinfo_basedata import OrderInfoBaseData


class OrderInfoDataDto:

    @staticmethod
    def from_entity(orderinfo: OrderInfoEntity) -> OrderInfoBaseData:
        info_model = OrderInfoBaseDataDto.from_entity(orderinfo.orderinfo)
        containers_model = OrderInfoContainerDataDto.from_entity(orderinfo.containers)
        model = OrderInfoData(info_model, containers_model)
        return model

    @staticmethod
    def to_entity(orderinfo: OrderInfoData) -> OrderInfoEntity:
        info_entity = OrderInfoBaseDataDto.to_entity(orderinfo.info)
        containers_entity = OrderInfoContainerDataDto.to_entity(orderinfo.containers)
        entity = OrderInfoEntity(info_entity, containers_entity)

        return entity
