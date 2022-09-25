import copy
from tms.applicationport.containers.common.containerdata import ContainerData


class ContainerGetAllOutputData:
    containers: list[ContainerData]

    def __init__(self, containers: list[ContainerData]):
        self.containers = copy.deepcopy(containers)
