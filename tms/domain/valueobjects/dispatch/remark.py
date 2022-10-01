from dataclasses import dataclass


@dataclass(init=False, eq=True)
class Remark:
    value: str = ""

    def __init__(self, value: str):
        self.value = value
