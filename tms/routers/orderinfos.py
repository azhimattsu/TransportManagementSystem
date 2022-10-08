from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from tms.utils.exception import CustomHttpException
from tms.domain.helpers.exception import DomainException

from tms.mysqlinfrastructure.mysql_orderinfo import MySqlOrderInfos

from tms.applicationport.orderinfos.common.orderinfo_basedata import OrderInfoBaseData
from tms.application.orderinfos.orderinfos_base_get_interactor import OrderInfosBaseGetInteractor
from tms.application.orderinfos.orderinfos_base_getall_interactor import OrderInfosBaseGetAllInteractor
from tms.application.orderinfos.orderinfos_base_post_interactor import OrderInfosBasePostInteractor
from tms.applicationport.orderinfos.post.orderinfo_base_post_inputdata import OrderInfoBasePostInputData
from tms.application.orderinfos.orderinfos_base_put_interactor import OrderInfosBasePutInteractor
from tms.applicationport.orderinfos.put.orderinfo_base_put_inputdata import OrderInfoBasePutInputData

from tms.application.orderinfos.orderinfos_get_interactor import OrderInfosGetInteractor

router = APIRouter()

# containerRep = MySqlContainers()
orderInfoRep = MySqlOrderInfos()
# dispatchInfoRep = MySqlDispatchInfos()


@router.get("/orderinfos/base/")
async def getOrderInfosBaseAllData():
    orderinfosGetUseCase = OrderInfosBaseGetAllInteractor(rep=orderInfoRep)
    orderinfos = orderinfosGetUseCase.fetch_all_data()
    return orderinfos


@router.get("/orderinfos/base/{slip_code}")
async def getOrderInfosBaseData(slip_code: str):
    orderinfosGetUseCase = OrderInfosBaseGetInteractor(rep=orderInfoRep)
    outputData = orderinfosGetUseCase.find_data_bycode(slip_code)
    if outputData.orderinfo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData


@router.post("/orderinfos/base/")
async def postOrderInfoBaseData(orderinfo: OrderInfoBaseData):
    try:
        orderinfosUseCase = OrderInfosBasePostInteractor(rep=orderInfoRep)
        command = OrderInfoBasePostInputData(orderinfo)
        orderinfosUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@router.put("/orderinfos/")
async def putOrderInfoData(orderinfo: OrderInfoBaseData):
    try:
        orderinfosUseCase = OrderInfosBasePutInteractor(rep=orderInfoRep)
        command = OrderInfoBasePutInputData(orderinfo)
        orderinfosUseCase.update_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@router.get("/orderinfos/{slip_code}")
async def getOrderInfosData(slip_code: str):
    orderinfosGetUseCase = OrderInfosGetInteractor(rep=orderInfoRep)
    outputData = orderinfosGetUseCase.find_data_bycode(slip_code)
    if outputData.orderinfo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData