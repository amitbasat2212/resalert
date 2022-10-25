
from urllib import response
from fastapi import FastAPI

app = FastAPI()

import uvicorn

from Routes import AutanticationRoute;
from Routes import JobsRoute;
from Routes import FinalStageRoute;
from Routes import CandidatesRoute;
from Routes import StatusRoute;


app.include_router(AutanticationRoute.router)
app.include_router(JobsRoute.router)
app.include_router(FinalStageRoute.router)
app.include_router(CandidatesRoute.router)
app.include_router(StatusRoute.router)


if __name__ == "__main__":
     uvicorn.run("Server:app", host="0.0.0.0", port=8010,reload=True)
