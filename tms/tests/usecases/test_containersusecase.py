
from ...infrastructure.inmemory.inmemorycontainer import InMemoryContainers
from ...usecases.containers.containersusecase import ContainersUsecase


def Test_ContainsersUsecase():
    usecase = ContainersUsecase(rep=InMemoryContainers())
    response = usecase.getAllData()
    print(response)


Test_ContainsersUsecase()
