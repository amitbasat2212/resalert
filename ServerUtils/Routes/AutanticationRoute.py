from fastapi import APIRouter, Request, Form

from fastapi.responses import FileResponse


<<<<<<< HEAD
router = APIRouter()


@router.post('/login')
async def login(username: str = Form(), password: str = Form()):
    return FileResponse('./client/index.html')
=======

router = APIRouter()

@router.get('/login')
def login(userName=None,password=None):
    return FileResponse('client/index.html')

>>>>>>> 93fb98e25d998279fa775f69fc6febacc968f1ec


@router.get('/logout')
def logout():

    pass
