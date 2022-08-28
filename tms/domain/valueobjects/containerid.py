from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class ContainerId:
    id: str = ""

    def __init__(self, id: str):
        object.__setattr__(self, "id", id)
