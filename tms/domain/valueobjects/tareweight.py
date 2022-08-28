from dataclasses import dataclass


@dataclass(init=False, eq=True, frozen=True)
class TareWeight:
    value: int = 0

    def __init__(self, value: int):
        object.__setattr__(self, "value", value)
