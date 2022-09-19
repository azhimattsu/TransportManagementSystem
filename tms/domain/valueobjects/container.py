from dataclasses import dataclass
from enum import IntEnum

from ...domain.helpers.exception import ArgumentOutRangeError
from ...domain.helpers.exception import ExceptionItemDetail


@dataclass(init=False, eq=True)
class Code:
    value: str = ""

    def __init__(self, value: str):
        if len(value) != 11:
            raise ArgumentOutRangeError("Validation Error",
                                        ExceptionItemDetail(
                                            "container",
                                            "code",
                                            value,
                                            "コンテナ番号は11桁で指定してください"))
        self.value = value


@dataclass(init=False, eq=True)
class TareWeight:
    value: int = 0

    def __init__(self, value: int):
        self.value = value


class Damage(IntEnum):
    DAMAGE_OK = 0
    DAMAGE_NG = 1


class Height(IntEnum):
    HEIGHT_NORMAL = 86
    HEIGHT_HIGH = 90


class Size(IntEnum):
    SIZE_NORMAL = 20
    SIZE_LONG = 40


class Type(IntEnum):
    TYPE_DRY = 1
    TYPE_REAFER = 2
    TYPE_OPENTOP = 3
    TYPE_FLAT = 4
    TYPE_TANK = 5
    TYPE_OTHER = 99
