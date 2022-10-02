
from tms.domain.valueobjects import container
import uuid


class CreateContainerService:

    @staticmethod
    def get_containerid() -> container.Id:
        return container.Id(str(uuid.uuid4()))
