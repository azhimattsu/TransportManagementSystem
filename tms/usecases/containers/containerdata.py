from dataclasses import dataclass

from ...domain.entities.container import Container


@dataclass(init=False, eq=True)
class ContainerData:
    code: str
    type: int
    tw: int
    height: int
    size: int
    damage: int

    def __init__(self, container: Container):
        self.code = container.code.value
        self.type = container.type.value
        self.tw = container.tw.value
        self.height = container.height.value
        self.size = container.size.value
        self.damage = container.damage.value
