
from urllib import response
from fastapi import FastAPI

app = FastAPI()

import uvicorn

from ServerUtils.Routes import AutanticationRoute;
from ServerUtils.Routes import JobsRoute;
from ServerUtils.Routes import CandidatesRoute;
from ServerUtils.Routes import StatusRouteAndStages;
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app.include_router(AutanticationRoute.router)
app.include_router(JobsRoute.router)
app.include_router(StatusRouteAndStages.router)
app.include_router(CandidatesRoute.router)

c
# app.mount("/client", StaticFiles(directory="client"), name="client")




# @app.get('/')
# def be():
#     return FileResponse('client/index.html')


if __name__ == "__main__":
     uvicorn.run("Server:app", host="0.0.0.0", port=8010,reload=True)
