from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

from tms.utils.exception import CustomHttpException
from tms.domain.models.shared import DomainException

from tms.infrastructure.mysql.mysql_container import MySqlContainer

from tms.application.containers.containers_get_interactor import ContainersGetInteractor
from tms.application.containers.containers_getall_interactor import ContainersGetAllInteractor
from tms.application.containers.containers_post_interactor import ContainersPostInteractor
from tms.application.containers.containers_put_interactor import ContainersPutInteractor

from tms.applicationport.container.shared.container_data import ContainerData
from tms.applicationport.container.post.container_post_input_data import ContainerPostInputData
from tms.applicationport.container.put.container_put_input_data import ContainerPutInputData

router = APIRouter()

containerRep = MySqlContainer()
# orderInfoRep = MySqlOrder()
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
