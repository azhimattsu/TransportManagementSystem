from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from tms.utils.exception import CustomHttpException
from tms.domain.helpers.exception import DomainException

from tms.mysqlinfrastructure.mysql_orderinfo import MySqlOrderInfos

from tms.applicationport.orderinfos.common.orderinfodata import OrderInfoData
from tms.application.orderinfos.orderinfos_get_interactor import OrderInfosGetInteractor
from tms.application.orderinfos.orderinfos_getall_interactor import OrderInfosGetAllInteractor
from tms.application.orderinfos.orderinfos_post_interactor import OrderInfosPostInteractor
from tms.applicationport.orderinfos.post.orderinfo_post_inputdata import OrderInfoPostInputData
from tms.application.orderinfos.orderinfos_put_interactor import OrderInfosPutInteractor
from tms.applicationport.orderinfos.put.orderinfo_put_inputdata import OrderInfoPutInputData

router = APIRouter()

# containerRep = MySqlContainers()
orderInfoRep = MySqlOrderInfos()
# dispatchInfoRep = MySqlDispatchInfos()


@router.get("/orderinfos/")
async def getOrderInfosAllData():
    orderinfosGetUseCase = OrderInfosGetAllInteractor(rep=orderInfoRep)
    orderinfos = orderinfosGetUseCase.fetch_all_data()
    return orderinfos


@router.get("/orderinfos/{slip_code}")
async def getOrderInfosData(slip_code: str):
    orderinfosGetUseCase = OrderInfosGetInteractor(rep=orderInfoRep)
    outputData = orderinfosGetUseCase.find_data_bycode(slip_code)
    if outputData.orderinfo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData


@router.post("/orderinfos/")
async def postOrderInfoData(orderinfo: OrderInfoData):
    try:
        orderinfosUseCase = OrderInfosPostInteractor(rep=orderInfoRep)
        command = OrderInfoPostInputData(orderinfo)
        orderinfosUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@router.put("/orderinfos/")
async def putOrderInfoData(orderinfo: OrderInfoData):
    try:
        orderinfosUseCase = OrderInfosPutInteractor(rep=orderInfoRep)
        command = OrderInfoPutInputData(orderinfo)
        orderinfosUseCase.update_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)