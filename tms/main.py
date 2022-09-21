import copy
from fastapi import FastAPI
from fastapi import status
from fastapi import Request
from fastapi import Response
from fastapi.responses import JSONResponse

from starlette.middleware.base import BaseHTTPMiddleware
from .master.domain.helpers.exception import DomainException

from tms.master.usecases.containers.post.containers_post_command import ContainersPostCommand
from tms.master.usecases.containers.containermodel import ContainerModel
from tms.master.infrastructure.inmemory.inmemory_container import InMemoryContainers
from tms.master.usecases.containers.get.containers_get_usecase import ContainersGetUsecase
from tms.master.usecases.containers.post.containers_post_usecase import ContainersPostUsecase


class CustomHttpException(Exception):
    status_code: int
    exception: DomainException
    detail: dict

    def __init__(self, status_code: int, exception: DomainException):
        self.status_code = status_code
        self.exception = copy.deepcopy(exception)
        self.detail = {
            "status": status_code,
            "message": exception.message,
        }
        if self.exception.detail is not None:
            detail1 = {
                    "item": self.exception.detail.item,
                    "field": self.exception.detail.field,
                    "value": self.exception.detail.value,
                    "message": self.exception.detail.message
            }
            self.detail["error"] = detail1
#        print(self.detail["errors"][0])


class HttpRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response: Response = await call_next(request)
        except CustomHttpException as ce:
            # カスタム例外
            response = JSONResponse(ce.detail, status_code=ce.status_code)

        return response


app = FastAPI()


@app.get("/")
async def index():
    return {"message: Hello World"}


@app.get("/containers/")
async def getContainersAllData():
    containrsGetUseCase = ContainersGetUsecase(rep=InMemoryContainers())
    containers = containrsGetUseCase.fetch_all_data()
    return containers


@app.get("/containers/{container_code}")
async def getContainersData(container_code: str):
    containrsGetUseCase = ContainersGetUsecase(rep=InMemoryContainers())
    container = containrsGetUseCase.find_data_bycode(container_code)
    return container


@app.put("/containers/")
async def putContainerData(container: ContainerModel):
    try:
        containrsUseCase = ContainersPostUsecase(rep=InMemoryContainers())
        command = ContainersPostCommand(container)
        containrsUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)

#        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,
#                            detail="TEST")


app.add_middleware(HttpRequestMiddleware)
