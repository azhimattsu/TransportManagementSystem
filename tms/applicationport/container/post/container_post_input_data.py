import copy
from tms.applicationport.container.shared.container_data import ContainerData


class ContainerPostInputData:
    container: ContainerData

    def __init__(self, container: ContainerData):
        self.container = copy.deepcopy(container)
