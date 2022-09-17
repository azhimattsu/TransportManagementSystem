from ...domain.valueobjects import container
from ...infrastructure.inmemory.inmemory_container import InMemoryContainers


def Test_InMemoryContainers_GetAllData():
    rep = InMemoryContainers()
    values = rep.GetAllData()
    length = len(values)
    print(length)
    print(values)


def Test_InMemoryContainers_GetData():
    rep = InMemoryContainers()
    value = rep.SearchDataByCode(container.Code("222222"))
    print(value)


Test_InMemoryContainers_GetAllData()
Test_InMemoryContainers_GetData()
