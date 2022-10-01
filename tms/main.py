import copy
from fastapi import HTTPException
from fastapi import FastAPI
from fastapi import status
from fastapi import Request
from fastapi import Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from tms.inmemoryinfrastructure.inmemory_container import InMemoryContainers
from tms.mysqlinfrastructure.mysql_container import MySqlContainers
from tms.mysqlinfrastructure.mysql_order import MySqlOrderInfos

from .domain.helpers.exception import DomainException

from tms.applicationport.containers.common.containerdata import ContainerData
from tms.application.containers.containers_get_interactor import ContainersGetInteractor
from tms.application.containers.containers_getall_interactor import ContainersGetAllInteractor
from tms.application.containers.containers_post_interactor import ContainersPostInteractor
from tms.applicationport.containers.post.container_post_inputdata import ContainerPostInputData
from tms.application.containers.containers_put_interactor import ContainersPutInteractor
from tms.applicationport.containers.put.container_put_inputdata import ContainerPutInputData

from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData
from tms.application.orderinfos.orderinfos_get_interactor import OrderInfosGetInteractor
from tms.application.orderinfos.orderinfos_getall_interactor import OrderInfosGetAllInteractor
from tms.application.orderinfos.orderinfos_post_interactor import OrderInfosPostInteractor
from tms.applicationport.orderinfos.post.orderinfo_post_inputdata import OrderInfoPostInputData
from tms.application.orderinfos.orderinfos_put_interactor import OrderInfosPutInteractor
from tms.applicationport.orderinfos.put.orderinfo_put_inputdata import OrderInfoPutInputData


class CustomHttpException(Exception):
    status_code: int
    exception: DomainException
    detail: dict

    def __init__(self, status_code: int, exception: DomainException):
        self.status_code = status_code
        self.exception = copy.deepcopy(exception)
        self.detail = {
            "detail": exception.message,
        }
        if self.exception.detail is not None:
            detail1 = {
                    "item": self.exception.detail.item,
                    "field": self.exception.detail.field,
                    "value": self.exception.detail.value,
                    "message": self.exception.detail.message
            }
            self.detail["error"] = detail1


class HttpRequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        try:
            response: Response = await call_next(request)
        except CustomHttpException as ce:
            # カスタム例外
            response = JSONResponse(ce.detail, status_code=ce.status_code)

        return response


containerRep = MySqlContainers()
orderInfoRep = MySqlOrderInfos()
#rep = InMemoryContainers()

app = FastAPI()


@app.get("/")
async def index():
    return {"message: Hello World"}


@app.get("/containers/")
async def getContainersAllData():
    containrsGetUseCase = ContainersGetAllInteractor(rep=containerRep)
    containers = containrsGetUseCase.fetch_all_data()
    return containers


@app.get("/containers/{container_code}")
async def getContainersData(container_code: str):
    containrsGetUseCase = ContainersGetInteractor(rep=containerRep)
    outputData = containrsGetUseCase.find_data_bycode(container_code)
    if outputData.container is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData


@app.post("/containers/")
async def postContainerData(container: ContainerData):
    try:
        containrsUseCase = ContainersPostInteractor(rep=containerRep)
        command = ContainerPostInputData(container)
        containrsUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@app.put("/containers/")
async def putContainerData(container: ContainerData):
    try:
        containrsUseCase = ContainersPutInteractor(rep=containerRep)
        command = ContainerPutInputData(container)
        containrsUseCase.update_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@app.get("/orderinfos/")
async def getOrderInfosAllData():
    orderinfosGetUseCase = OrderInfosGetAllInteractor(rep=orderInfoRep)
    orderinfos = orderinfosGetUseCase.fetch_all_data()
    return orderinfos


@app.get("/orderinfos/{slip_code}")
async def getOrderInfosData(slip_code: str):
    orderinfosGetUseCase = OrderInfosGetInteractor(rep=orderInfoRep)
    outputData = orderinfosGetUseCase.find_data_bycode(slip_code)
    if outputData.orderinfo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData


@app.post("/orderinfos/")
async def postOrderInfoData(orderinfo: OrderInfoData):
    try:
        orderinfosUseCase = OrderInfosPostInteractor(rep=orderInfoRep)
        command = OrderInfoPostInputData(orderinfo)
        orderinfosUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@app.put("/orderinfos/")
async def putOrderInfoData(orderinfo: OrderInfoData):
    try:
        orderinfosUseCase = OrderInfosPutInteractor(rep=orderInfoRep)
        command = OrderInfoPutInputData(orderinfo)
        orderinfosUseCase.update_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)

app.add_middleware(HttpRequestMiddleware)
