import imp


import copy
from tms.usecases.containers.containerdata import ContainerData


class ContainerGetAllResult:
    containers: list[ContainerData]

    def __init__(self, containers: list[ContainerData]):
        self.containers = copy.deepcopy(containers)

