from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from tms.infrastructure.mysql.mysql_order import MySqlOrder

from tms.application.orders.order_get_interactor import OrderGetInteractor

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
