from ...infrastructure.inmemory.inmemorycontainer import InMemoryContainers


def Test_InMemoryContainers():
    rep = InMemoryContainers()
    values = rep.GetAllData()
    length = len(values)
    print(length)
    print(values)


Test_InMemoryContainers()
