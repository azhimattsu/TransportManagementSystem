from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class ContainerCode:
    value: str = ""

    def __init__(self, value: str):
        object.__setattr__(self, "value", value)

    @property
    def container_code(self) -> str:
        return self.value
