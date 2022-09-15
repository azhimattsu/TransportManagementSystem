from fastapi import FastAPI

from .infrastructure.inmemory.inmemory_container import InMemoryContainers
from .usecases.containers.get.containers_usecase import ContainersUsecase

app = FastAPI()


@app.get("/")
async def index():
    return {"message: Hello World"}


@app.get("/containers/")
async def getContainersAllData():
    containrsGetUseCase = ContainersUsecase(rep=InMemoryContainers())
    containers = containrsGetUseCase.getAllData()
    return containers


@app.get("/containers/{container_code}")
async def getContainersData(container_code: str):
    containrsGetUseCase = ContainersUsecase(rep=InMemoryContainers())
    container = containrsGetUseCase.getData(container_code)
    return container
