from fastapi import Request
from fastapi import APIRouter

from ServerUtils.queries import CandidateQueries;

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"]
)


@router.get('/')
def get_candidates_of_jobs():
    candidates=CandidateQueries.get_candidates_of_all_jobs();
    return candidates;


@router.get('/{job_id}')
def get_candidates_of_jobs(job_id):
    candidates=CandidateQueries.get_candidates_of_job_by_id(job_id);
    return candidates;

@router.post('/')
async def add_candidate (request: Request): 
    candidate =await request.json()
    new_candidate=CandidateQueries.add_candidate_user(candidate)
    return new_candidate;



    
    
