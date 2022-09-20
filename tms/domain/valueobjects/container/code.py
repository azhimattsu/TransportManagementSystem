from dataclasses import dataclass
from ....domain.helpers.exception import ArgumentOutRangeError
from ....domain.helpers.exception import ExceptionItemDetail


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
