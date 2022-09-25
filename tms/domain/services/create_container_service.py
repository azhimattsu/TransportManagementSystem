
from tms.domain.valueobjects import container
import uuid


class CreateContainerService:

    @staticmethod
    def GetContainerId() -> container.Id:
        return container.Id(str(uuid.uuid4()))
