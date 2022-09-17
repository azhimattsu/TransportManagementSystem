import copy
from ..containerdata import ContainerData


class ContainersGetAllResult:
    containers: list[ContainerData]

    def __init__(self, containers: list[ContainerData]):
        self.containers = copy.deepcopy(containers)
