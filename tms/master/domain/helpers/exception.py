
import copy


class ExceptionItemDetail:
    item: str
    field: str
    value: str
    message: str

    def __init__(self, item: str, field: str, value: str, message: str):
        self.item = item
        self.field = field
        self.value = value
        self.message = message


class DomainException(Exception):
    message: str
    detail: ExceptionItemDetail = None

    def __init__(self, message: str, itemdetail: ExceptionItemDetail = None):
        self.message = message
        if itemdetail is not None:
            self.detail = copy.deepcopy(itemdetail)


class ArgumentOutRangeError(DomainException):
    pass
