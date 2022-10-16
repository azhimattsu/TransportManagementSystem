from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status


from tms.domain.models.shared.exception import DomainException
from tms.utils.exception import CustomHttpException
from tms.infrastructure.mysql.mysql_order import MySqlOrder

from tms.application.orders.order_get_interactor import OrderGetInteractor
from tms.application.orders.order_detail_post_interactor import OrderDetailPostInteractor
from tms.application.orders.order_detail_get_interactor import OrderDetailGetInteractor
from tms.application.orders.order_detail_put_interactor import OrderDetailPutInteractor

from tms.applicationport.order.shared.order_detail_data import OrderDetailData
from tms.applicationport.order.post.order_detail_post_input_data import OrderDetailPostInputData
from tms.applicationport.order.put.order_detail_put_input_data import OrderDetailPutInputData

router = APIRouter()

# containerRep = MySqlContainers()
ordersRep = MySqlOrder()
# dispatchInfoRep = MySqlDispatchInfos()


@router.get("/orders/{slip_code}")
async def getOrderData(slip_code: str):
    orderinfosGetUseCase = OrderGetInteractor(rep=ordersRep)
    outputData = orderinfosGetUseCase.find_data_bycode(slip_code)
    if outputData.orderinfo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData.orderinfo

@router.get("/orders/detail/{order_id}")
async def getOrderInfosBaseData(order_id: str):
    orderinfosGetUseCase = OrderDetailGetInteractor(rep=ordersRep)
    outputData = orderinfosGetUseCase.find_data_byid(order_id)
    if outputData.orderinfo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData.orderinfo


@router.post("/orders/detail/")
async def postOrderDetailData(orderinfo: OrderDetailData):
    try:
        orderinfosUseCase = OrderDetailPostInteractor(rep=ordersRep)
        command = OrderDetailPostInputData(orderinfo)
        orderinfosUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@router.put("/orders/detail/")
async def putOrderDetailData(orderinfo: OrderDetailData):
    try:
        orderinfosUseCase = OrderDetailPutInteractor(rep=ordersRep)
        command = OrderDetailPutInputData(orderinfo)
        orderinfosUseCase.update_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)
