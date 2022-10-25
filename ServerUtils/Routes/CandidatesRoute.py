from fastapi import APIRouter

from ServerUtils.queries import candidateQueries;

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"]
)



@router.get('/')
def get_candidates_of_jobs():
    candidates=candidateQueries.get_candidates_of_all_jobs();
    return candidates;


@router.get('/{job_id}')
def get_candidates_of_jobs(job_id):
    candidates=candidateQueries.get_candidates_of_job_by_id(job_id);
    return candidates;

@router.post('/')
def add_candidate (candidate):    
    new_candidate=candidateQueries.add_candidate(candidate)
    return new_candidate;



    
    
