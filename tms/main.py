from fastapi import FastAPI

from tms.routers import containers, orderinfos, dispatchinfos
# from tms.inmemoryinfrastructure.inmemory_container import InMemoryContainers
from tms.utils.httpmiddleware import HttpRequestMiddleware


app = FastAPI()

app.include_router(containers.router)
app.include_router(orderinfos.router)
app.include_router(dispatchinfos.router)

app.add_middleware(HttpRequestMiddleware)


@app.get("/")
async def index():
    return {"message: Hello World"}
