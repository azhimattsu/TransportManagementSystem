from ...domain.valueobjects.containercode import ContainerCode
from ...infrastructure.inmemory.inmemory_container import InMemoryContainers


def Test_InMemoryContainers_GetAllData():
    rep = InMemoryContainers()
    values = rep.GetAllData()
    length = len(values)
    print(length)
    print(values)


def Test_InMemoryContainers_GetData():
    rep = InMemoryContainers()
    value = rep.SearchDataByCode(ContainerCode("222222"))
    print(value)


Test_InMemoryContainers_GetAllData()
Test_InMemoryContainers_GetData()
