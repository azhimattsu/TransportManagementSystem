from dataclasses import dataclass

from ...domain.entities.container import Container


@dataclass(init=False, eq=True, frozen=True)
class ContainerData:
    code: str
    type: int
    tw: int
    height: int
    size: int

    def __init__(self, container: Container):
        print(container.code.container_code)
#        print(container.code)
#        self.code = container.code.value
#        self.type = container.type.value
#        self.tw = container.tw.value
#        self.height = container.height.value
#        self.size = container.size.value
