
from ...infrastructure.inmemory.inmemorycontainer import InMemoryContainers
from ...usecases.containers.containersusecase import ContainersUsecase


def Test_ContainersUsecase():
    usecase = ContainersUsecase(rep=InMemoryContainers())
    response = usecase.getAllData()

    for i in response.containers:
        print(i.code)


Test_ContainersUsecase()
