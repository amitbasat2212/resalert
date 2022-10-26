from fastapi import APIRouter, Request, Form

from fastapi.responses import FileResponse


router = APIRouter()


@router.post('/login')
async def login(username: str = Form(), password: str = Form()):
    return FileResponse('./client/index.html')


@router.get('/logout')
def logout():

    pass
