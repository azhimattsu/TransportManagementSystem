import copy
from typing import Optional
from tms.applicationport.containers.common.containerdata import ContainerData


class ContainerGetOutputData:
    container: Optional[ContainerData]

    def __init__(self, container: ContainerData):
        self.container = copy.deepcopy(container)
