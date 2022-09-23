from tms.master.domain.valueobjects import container
from tms.master.infrastructure.inmemory.inmemory_container import InMemoryContainers


def Test_InMemoryContainers_GetAllData():
    rep = InMemoryContainers()
    values = rep.fetch_all_data()
    length = len(values)
    print(length)
    print(values)


def Test_InMemoryContainers_GetData():
    rep = InMemoryContainers()
    value = rep.find_data_bycode(container.Code("222222"))
    print(value)


Test_InMemoryContainers_GetAllData()
Test_InMemoryContainers_GetData()
