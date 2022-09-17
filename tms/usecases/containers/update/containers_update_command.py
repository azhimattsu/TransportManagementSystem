import copy
from ..containermodel import ContainerModel


class ContainersUpdateCommand:
    container: ContainerModel

    def __init__(self, container: ContainerModel):
        self.container = copy.deepcopy(container)
