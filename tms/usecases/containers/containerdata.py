from ...domain.entities.container import Container


class ContainerData:
    code: str
    type: int
    tw: int
    height: int
    size: int

    def __init__(self, container: Container):
        self.code = container.code.value
        self.type = container.type.value
        self.tw = container.tw.value
        self.height = container.height.value
        self.size = container.size.value
