from fastapi import APIRouter



# from TypesOfObject import Candidate
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
    new_candidate =Candiddate(candidate.first_name,
    candidate.last_name,candidate.mail,
    candidate.cv,
    candidate.job,
    candidate.status,
    candidate.stage,
    candidate.gender)



    
    
