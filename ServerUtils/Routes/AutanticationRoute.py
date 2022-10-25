from fastapi import APIRouter

from fastapi.responses import FileResponse



router = APIRouter(
    prefix="/autantiction",
    tags=["autantiction"]
)


@router.get('/')
def login(userName=None,password=None):
    return FileResponse('client/index.html')



@router.get('/logout')
def logout():
   
    pass