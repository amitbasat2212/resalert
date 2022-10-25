from fastapi import APIRouter

from fastapi.responses import FileResponse



router = APIRouter(
    prefix="/autantiction",
    tags=["autantiction"]
)


@router.get('/index')
def login():
    return FileResponse('client/index.html')



@router.get('/logout')
def logout():
   
    pass