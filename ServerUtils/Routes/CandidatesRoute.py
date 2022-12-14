from os import stat
from fastapi import Request
from fastapi import APIRouter

from ServerUtils.queries import CandidateQueries;

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"]
)

 



@router.get('/')
def get_candidates_of_jobs(job_name ="", status ="", stage ="", gender =""):
    list_of_filters=CandidateQueries.get_candidates_of_all_jobs();    

    if job_name != "":        
        list_of_filters=[p for p in list_of_filters if p.job == job_name]

    if status  != "":
        list_of_filters=[p for p in list_of_filters if p.status == status]       
     
       
    if stage  != "":  
       list_of_filters=[p for p in list_of_filters if p.stage == stage]        
    
     
    if gender != "": 
       list_of_filters=[p for p in list_of_filters if p.Gender == gender]       
       
    if  gender  == "" and stage  == "" and status  == "" and job_name  == "":
        list_of_filters=CandidateQueries.get_candidates_of_all_jobs();
    
    return list_of_filters;
    



@router.post('/')
async def add_candidate (request: Request): 
    candidate =await request.json()
    new_candidate=CandidateQueries.add_candidate_user(candidate)
    return new_candidate;

@router.post('/jobs')
async def add_candidate_to_jobs(candidate_email,job_id): 
    new_candidate_to_job =CandidateQueries.add_candidate_to_a_job(candidate_email,job_id);    
    return new_candidate_to_job;
    


    
    
