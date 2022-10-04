from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from tms.utils.exception import CustomHttpException
from tms.domain.helpers.exception import DomainException

from tms.mysqlinfrastructure.mysql_container import MySqlContainers

from tms.applicationport.containers.common.containerdata import ContainerData
from tms.application.containers.containers_get_interactor import ContainersGetInteractor
from tms.application.containers.containers_getall_interactor import ContainersGetAllInteractor
from tms.application.containers.containers_post_interactor import ContainersPostInteractor
from tms.applicationport.containers.post.container_post_inputdata import ContainerPostInputData
from tms.application.containers.containers_put_interactor import ContainersPutInteractor
from tms.applicationport.containers.put.container_put_inputdata import ContainerPutInputData

router = APIRouter()

containerRep = MySqlContainers()
# orderInfoRep = MySqlOrderInfos()
# dispatchInfoRep = MySqlDispatchInfos()


@router.get("/containers/")
async def getContainersAllData():
    containrsGetUseCase = ContainersGetAllInteractor(rep=containerRep)
    containers = containrsGetUseCase.fetch_all_data()
    return containers


@router.get("/containers/{container_code}")
async def getContainersData(container_code: str):
    containrsGetUseCase = ContainersGetInteractor(rep=containerRep)
    outputData = containrsGetUseCase.find_data_bycode(container_code)
    if outputData.container is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return outputData


@router.post("/containers/")
async def postContainerData(container: ContainerData):
    try:
        containrsUseCase = ContainersPostInteractor(rep=containerRep)
        command = ContainerPostInputData(container)
        containrsUseCase.create_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)


@router.put("/containers/")
async def putContainerData(container: ContainerData):
    try:
        containrsUseCase = ContainersPutInteractor(rep=containerRep)
        command = ContainerPutInputData(container)
        containrsUseCase.update_data(command)
    except DomainException as e:
        raise CustomHttpException(status_code=status.HTTP_400_BAD_REQUEST,
                                  exception=e)
