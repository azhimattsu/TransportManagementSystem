from ...domain.valueobjects.containerid import ContainerId


def Test_ContainerId():
    containerid = ContainerId("123456")
    print(containerid)


print("TEST")
Test_ContainerId()
