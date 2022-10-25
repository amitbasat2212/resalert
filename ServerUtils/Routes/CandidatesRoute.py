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

@router.post('/')
def add_candidate (candidate):    
    new_candidate=candidateQueries.add_candidate(candidate)
    return new_candidate;



    
    
