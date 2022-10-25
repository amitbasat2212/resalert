from fastapi import APIRouter





router = APIRouter(
    prefix="/autantiction",
    tags=["autantiction"]
)


@router.get('/login')
def login():
     
    pass

@router.get('/logout')
def logout():
    #return the candidates of the jobs 
    pass