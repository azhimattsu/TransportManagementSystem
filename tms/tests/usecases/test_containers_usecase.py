
from ...infrastructure.inmemory.inmemory_container import InMemoryContainers
from ...usecases.containers.containers_usecase import ContainersUsecase


def Test_ContainersUsecase_GetAllData():
    usecase = ContainersUsecase(rep=InMemoryContainers())
    response = usecase.fetch_all_data()

    for i in response.containers:
        print(i.code)


def Test_ContainersUsecase_GetData():
    usecase = ContainersUsecase(rep=InMemoryContainers())
    response = usecase.find_data_bycode("222222")
    print(response.container.code)


Test_ContainersUsecase_GetAllData()
Test_ContainersUsecase_GetData()
