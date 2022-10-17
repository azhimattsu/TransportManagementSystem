from tms.applicationport.order.shared.order_detail_data_dto import OrderDetailDataDto
from tms.applicationport.order.shared.order_container_data_dto import OrderContainerDataDto
from tms.applicationport.order.shared.order_data import OrderData
from tms.domain.models.order import OrderInfo
from .order_detail_data import OrderDetailData


class OrderDataDto:

    @staticmethod
    def from_entity(orderinfo: OrderInfo) -> OrderDetailData:
        info_model = OrderDetailDataDto.from_entity(orderinfo.detail_info)
        containers_model = OrderContainerDataDto.from_entity(orderinfo.arrangement_info.containers)
        model = OrderData(info_model, containers_model)
        return model

    @staticmethod
    def to_entity(orderinfo: OrderData) -> OrderInfo:
        info_entity = OrderDetailDataDto.to_entity(orderinfo.detail)
        containers_entity = OrderContainerDataDto.to_entity(orderinfo.containers)
        entity = OrderInfo(info_entity, containers_entity)

        return entity
