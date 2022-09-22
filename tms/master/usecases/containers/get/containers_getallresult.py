import copy
from tms.master.usecases.containers.containermodel import ContainerModel


class ContainersGetAllResult:
    containers: list[ContainerModel]

    def __init__(self, containers: list[ContainerModel]):
        self.containers = copy.deepcopy(containers)
