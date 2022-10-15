import copy
from tms.applicationport.container.shared.container_data import ContainerData


class ContainerGetAllOutputData:
    containers: list[ContainerData]

    def __init__(self, containers: list[ContainerData]):
        self.containers = copy.deepcopy(containers)
