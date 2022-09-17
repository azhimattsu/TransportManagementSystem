import copy
from ..containerdata import ContainerData


class ContainersUpdateCommand:
    container: ContainerData

    def __init__(self, container: ContainerData):
        self.container = copy.deepcopy(container)
