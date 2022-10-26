from fastapi import APIRouter

from fastapi.responses import FileResponse



router = APIRouter()

@router.get('/login')
def login(userName=None,password=None):
    return FileResponse('client/index.html')



@router.get('/logout')
def logout():
   
    pass