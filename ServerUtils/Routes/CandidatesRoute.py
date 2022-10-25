from fastapi import APIRouter




from SqlUtils.queries import candidateQueries;

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"]
)



@router.get('/')
def get_candidates_of_jobs(job_id):
    candidates=candidateQueries.get_candidates_of_jobs(job_id)
    return candidates;

# @router.post('/')
# def add_candidate (candidate):    
#     candidate=candidateQueries.
#     return new_candidate;



    
    
