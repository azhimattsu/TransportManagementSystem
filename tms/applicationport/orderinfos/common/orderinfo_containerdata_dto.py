from tms.applicationport.orderinfos.common.orderinfo_containerdata import OrderInfoContainerData
from tms.domain.entities.orderinfo_container import OrderInfoContainerEntity
from tms.domain.valueobjects import common, container
from tms.domain.valueobjects import order


class OrderInfoContainerDataDto:

    @staticmethod
    def from_entity(containers: list[OrderInfoContainerEntity]) -> list[OrderInfoContainerData]:
        results: list[OrderInfoContainerData] = []
        results.clear()

        for item in containers:
            model = OrderInfoContainerData(item.order_id.value,
                                           item.index,
                                           item.container_id.value,
                                           item.container_code.value,
                                           item.type,
                                           item.tw.value,
                                           item.height.value,
                                           item.size.value,
                                           item.damage.value,
                                           item.freight,
                                           item.surcharge,
                                           item.other,
                                           item.create_user.value,
                                           item.update_user.value,
                                           item.create_at.getStr(),
                                           item.update_at.getStr())
            results.append(model)

        return results

    @staticmethod
    def to_entity(orderinfocontainers: list[OrderInfoContainerData]) -> list[OrderInfoContainerEntity]:
        results: list[OrderInfoContainerEntity] = []
        results.clear()

        for item in orderinfocontainers:
            item = OrderInfoContainerEntity(order.Id(item.order_id),
                                            item.index,
                                            container.Id(item.container_id),
                                            container.Code(item.container_code),
                                            container.Type(item.type),
                                            container.TareWeight(item.tw),
                                            container.Height(item.height),
                                            container.Size(item.size),
                                            container.Damage(item.damage),
                                            item.freight,
                                            item.surcharge,
                                            item.other,
                                            common.MailAddress(item.create_user),
                                            common.MailAddress(item.update_user),
                                            common.CreateDateTime(item.create_at),
                                            common.CreateDateTime(item.update_at))

            results.append(item)

        return results
