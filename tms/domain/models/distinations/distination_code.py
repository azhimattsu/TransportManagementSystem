from dataclasses import dataclass


@dataclass(init=False, eq=True)
class DistinationCode:
    value: str = ""

    def __init__(self, value: str):
        self.value = value
