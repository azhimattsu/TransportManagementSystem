import copy
from fastapi import FastAPI
from fastapi import status
from fastapi import Request
from fastapi import Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from tms.inmemoryinfrastructure.inmemory_container import InMemoryContainers
from tms.mysqlinfrastructure.mysql_container import MySqlContainers

from .domain.helpers.exception import DomainException
from tms.applicationport.containers.common.containerdata import ContainerData

from tms.application.containers.containers_post_interactor import ContainersPostInteractor
from tms.applicationport.containers.post.container_post_inputdata import ContainerPostInputData

from tms.application.containers.containers_get_interactor import ContainersGetInteractor
from tms.application.containers.containers_getall_interactor import ContainersGetAllInteractor


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

rep = MySqlContainers()
#rep = InMemoryContainers()

app = FastAPI()


@app.get("/")
async def index():
    return {"message: Hello World"}


@app.get("/containers/")
async def getContainersAllData():
    containrsGetUseCase = ContainersGetAllInteractor(rep=rep)
    containers = containrsGetUseCase.fetch_all_data()
    return containers


@app.get("/containers/{container_code}")
async def getContainersData(container_code: str):
    containrsGetUseCase = ContainersGetInteractor(rep=rep)
    container = containrsGetUseCase.find_data_bycode(container_code)
    return container


@app.put("/containers/")
async def putContainerData(container: ContainerData):
    try:
        containrsUseCase = ContainersPostInteractor(rep=rep)
        command = ContainerPostInputData(container)
        containrsUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)

#        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,
#                            detail="TEST")


app.add_middleware(HttpRequestMiddleware)
