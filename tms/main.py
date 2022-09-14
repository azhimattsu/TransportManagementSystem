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
