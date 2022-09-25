from dataclasses import dataclass


@dataclass(init=False, eq=True)
class SlipCode:
    value: str = ""

    def __init__(self, value: str):
        self.value = value
