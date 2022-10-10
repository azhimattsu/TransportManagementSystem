from dataclasses import dataclass
from tms.domain.valueobjects import container
from tms.domain.valueobjects import common
from tms.domain.valueobjects import order


@dataclass(init=False, eq=True)
class OrderInfoContainerEntity():
    order_id: order.Id
    sort_id: int
    container_id: container.Id
    freight: int
    surcharge: int
    other: int
    create_user: common.MailAddress
    update_user: common.MailAddress
    create_at: common.CDateTime
    update_at: common.CDateTime

    def __init__(self,
                 order_id: order.Id,
                 sort_id: int,
                 container_id: container.Id,
                 freight: int,
                 surcharge: int,
                 other: int,
                 create_user: common.MailAddress,
                 update_user: common.MailAddress,
                 create_at: common.CDateTime,
                 update_at: common.CDateTime):
        self.order_id = order_id
        self.sort_id = sort_id
        self.container_id = container_id
        self.freight = freight
        self.surcharge = surcharge
        self.other = other
        self.create_user = create_user
        self.update_user = update_user
        self.create_at = create_at
        self.update_at = update_at
