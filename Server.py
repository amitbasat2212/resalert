from ServerUtils.Routes import StatusRouteAndStages
from ServerUtils.Routes import CandidatesRoute
from ServerUtils.Routes import JobsRoute
from ServerUtils.Routes import AutanticationRoute
from ServerUtils.Routes import StaticsRoute
from ServerUtils.queries import initialize_tables
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from urllib import response
from fastapi import FastAPI

app = FastAPI()


app.include_router(AutanticationRoute.router)
app.include_router(JobsRoute.router)
app.include_router(StatusRouteAndStages.router)
app.include_router(StaticsRoute.router)
app.include_router(CandidatesRoute.router)


app.mount("/client", StaticFiles(directory="client"), name="client")


@app.get('/')
def be():
    return FileResponse('client/index.html')

@app.get('/create')
def create():
    initialize_tables.init_the_database()


if __name__ == "__main__":
    uvicorn.run("Server:app", host="0.0.0.0", port=8060, reload=True)
