import copy
from typing import Optional
from tms.applicationport.container.shared.container_data import ContainerData


class ContainerGetOutputData:
    container: Optional[ContainerData]

    def __init__(self, container: ContainerData):
        self.container = copy.deepcopy(container)
