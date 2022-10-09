from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from tms.utils.exception import CustomHttpException
from tms.domain.helpers.exception import DomainException

from tms.mysqlinfrastructure.mysql_dispatchinfo import MySqlDispatchInfos

from tms.applicationport.dispatchinfos.common.dispatchinfodata import DispatchInfoData
from tms.application.dispatchinfos.dispatchinfos_get_interactor import DispatchInfosGetInteractor
from tms.application.dispatchinfos.dispatchinfos_getall_interactor import DispatchInfosGetAllInteractor
from tms.application.dispatchinfos.dispatchinfos_post_interactor import DispatchInfosPostInteractor
from tms.applicationport.dispatchinfos.post.dispatchinfo_post_inputdata import DispatchInfoPostInputData
from tms.application.dispatchinfos.dispatchinfos_put_interactor import DispatchInfosPutInteractor
from tms.applicationport.dispatchinfos.put.dispatchinfo_put_inputdata import DispatchInfoPutInputData

router = APIRouter()

# containerRep = MySqlContainers()
# orderInfoRep = MySqlOrderInfos()
dispatchInfoRep = MySqlDispatchInfos()


@router.get("/dispatchinfos/")
async def getDispatchInfosAllData():
    dispatchinfosGetUseCase = DispatchInfosGetAllInteractor(rep=dispatchInfoRep)
    dispatchinfos = dispatchinfosGetUseCase.fetch_all_data()
    return dispatchinfos


@router.get("/dispatchinfos/{slip_code}")
async def getDispatchInfosData(slip_code: str):
    dispatchinfosGetUseCase = DispatchInfosGetInteractor(rep=dispatchInfoRep)
    outputData = dispatchinfosGetUseCase.find_data_byid(slip_code)
    if outputData.orderinfo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData


@router.post("/dispatchinfos/")
async def postDispatchInfoData(dispatchinfo: DispatchInfoData):
    try:
        dispatchinfosUseCase = DispatchInfosPostInteractor(rep=dispatchInfoRep)
        command = DispatchInfoPostInputData(dispatchinfo)
        dispatchinfosUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@router.put("/dispatchinfos/")
async def putDispatchInfoData(dispatchinfo: DispatchInfoData):
    try:
        dispatchinfosUseCase = DispatchInfosPutInteractor(rep=dispatchInfoRep)
        command = DispatchInfoPutInputData(dispatchinfo)
        dispatchinfosUseCase.update_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)