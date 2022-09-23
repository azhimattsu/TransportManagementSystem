import copy
from tms.master.usecases.containers.containermodel import ContainerModel


class ContainersPostCommand:
    container: ContainerModel

    def __init__(self, container: ContainerModel):
        self.container = copy.deepcopy(container)
