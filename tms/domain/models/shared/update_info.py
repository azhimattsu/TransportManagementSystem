from dataclasses import dataclass

from tms.domain.models import shared


@dataclass(init=False, eq=True)
class UpdateInfo:
    create_user: shared.MailAddress
    update_user: shared.MailAddress
    create_at: shared.CDateTime
    update_at: shared.CDateTime

    def __init__(self,
                 create_user: shared.MailAddress,
                 update_user: shared.MailAddress,
                 create_at: shared.CDateTime,
                 update_at: shared.CDateTime,
                 ):
        self.create_user = create_user
        self.update_user = update_user
        self.create_at = create_at
        self.update_at = update_at
