

class DomainException(Exception):
    kind: str
    item: str
    value: str
    message: str

    def __init__(self, kind: str, item: str, value: str, message: str):
        self.kind = kind
        self.item = item
        self.value = value
        self.message = message

#    def __str__(self):
#        return "{0} ({1}) kind:{2} item:{3}".format(self.message,
#                                                    self.value,
#                                                    self.kind,
#                                                    self.item)

    def getMessage(self):
        return "{0} ({1}) kind:{2} item:{3}".format(self.message,
                                                    self.value,
                                                    self.kind,
                                                    self.item)


class ArgumentOutRangeError(DomainException):
    pass
