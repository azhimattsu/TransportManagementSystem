
from tms.domain.models import container
import uuid


class CreateContainerService:

    @staticmethod
    def get_containerid() -> container.ContainerId:
        return container.ContainerId(str(uuid.uuid4()))
