import copy
from tms.usecases.containers.containerdata import ContainerData


class ContainersGetResult:
    container: ContainerData

    def __init__(self, container: ContainerData):
        self.container = copy.deepcopy(container)
