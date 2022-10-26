from fastapi import APIRouter, Request, Form

from fastapi.responses import FileResponse



router = APIRouter()

@router.get('/login')
def login(userName=None,password=None):
    return FileResponse('client/index.html')



@router.get('/logout')
def logout():

    pass
