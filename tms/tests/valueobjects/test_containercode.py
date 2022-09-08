from ...domain.valueobjects.containercode import ContainerCode


def Test_ContainerCode():
    containercode = ContainerCode("123456")
    print(containercode.value)


def Test_ContainerCode_ng1():
    containercode = ContainerCode("")
    containercode.value = "AAAAAA"
    print(containercode)


print("TEST")
Test_ContainerCode()
# Test_ContainerCode_ng1()
