import copy
from ..containermodel import ContainerModel


class ContainersGetResult:
    container: ContainerModel

    def __init__(self, container: ContainerModel):
        self.container = copy.deepcopy(container)
