from ...domain.valueobjects import container


def Test_ContainerCode():
    containercode = container.Code("123456")
    print(containercode.value)


def Test_ContainerCode_ng1():
    containercode = container.Code("")
    containercode.value = "AAAAAA"
    print(containercode)


print("TEST")
Test_ContainerCode()
# Test_ContainerCode_ng1()
