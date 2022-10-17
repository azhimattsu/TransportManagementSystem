import copy
from tms.domain.models.shared.exception import DomainException


class CustomHttpException(Exception):
    status_code: int
    exception: DomainException
    detail: dict

    def __init__(self, status_code: int, exception: DomainException):
        self.status_code = status_code
        self.exception = copy.deepcopy(exception)
        self.detail = {
            "detail": exception.message,
        }
        if self.exception.detail is not None:
            detail1 = {
                    "item": self.exception.detail.item,
                    "field": self.exception.detail.field,
                    "value": self.exception.detail.value,
                    "message": self.exception.detail.message
            }
            self.detail["error"] = detail1
