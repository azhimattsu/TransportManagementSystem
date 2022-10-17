from tms.applicationport.order.shared.order_container_data import OrderContainerData
from tms.domain.models import container
from tms.domain.models import order
from tms.domain.models import shared


class OrderContainerDataDto:

    @staticmethod
    def from_entity(containers: list[order.ContainerRow]) -> list[OrderContainerData]:
        results: list[OrderContainerData] = []
        results.clear()
        for item in containers:
            model = OrderContainerData(item.order_id.value,
                                       item.sort_id,
                                       item.container_id.value,
                                       item.freight,
                                       item.surcharge,
                                       item.other,
                                       item.update_info.create_user.value,
                                       item.update_info.update_user.value,
                                       item.update_info.create_at.getStr(),
                                       item.update_info.update_at.getStr())
            print(model)
            results.append(model)

        return results

    @staticmethod
    def to_entity(orderinfocontainers: list[OrderContainerData]) -> list[order.ContainerRow]:
        results: list[order.ContainerRow] = []
        results.clear()

        for item in orderinfocontainers:
            item = order.ContainerRow(order.OrderId(item.order_id),
                                      item.sort_id,
                                      container.ContainerId(item.container_id),
                                      item.freight,
                                      item.surcharge,
                                      item.other,
                                      shared.UpdateInfo(shared.MailAddress(item.create_user),
                                                        shared.MailAddress(item.update_user),
                                                        shared.CDateTime(item.create_at),
                                                        shared.CDateTime(item.update_at)))

            results.append(item)

        return results
