import copy
from tms.applicationport.containers.common.containerdata import ContainerData


class ContainerPostInputData:
    container: ContainerData

    def __init__(self, container: ContainerData):
        self.container = copy.deepcopy(container)
