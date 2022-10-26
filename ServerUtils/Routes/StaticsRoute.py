from fastapi import APIRouter,Request


from ServerUtils.queries import StaticQueries;


router = APIRouter(
    prefix="/statics",
    tags=["statics"]
)

@router.get('/Gender')
def get_group_per_gender():
    numers_per_gender=StaticQueries.get_numberes_per_gender()
    return numers_per_gender;

@router.get('/dep')
def get_group_per_gender():
    numers_per_gender=StaticQueries.get_numberes_per_gender()
    return numers_per_gender;
