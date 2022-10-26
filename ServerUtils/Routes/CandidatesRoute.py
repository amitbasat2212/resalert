from os import stat
from fastapi import Request
from fastapi import APIRouter

from ServerUtils.queries import CandidateQueries;

router = APIRouter(
    prefix="/candidates",
    tags=["candidates"]
)


def add_items_to_list(result): 
    list_of_item_to_return=[]             
    for item in result:
        list_of_item_to_return.append(item)     
                         
    return list_of_item_to_return;       


      


def check_if_empty(array_result):
    if(len(array_result)==0):
        return True;




@router.get('/')
def get_candidates_of_jobs(job_id ="", status ="", stage ="", gender =""):
    list_of_filters=CandidateQueries.get_candidates_of_all_jobs();    

    if job_id != "":
        list_of_filters=[p for p in list_of_filters if p.job == int(job_id)]

    if status  != "":
        list_of_filters=[p for p in list_of_filters if p.status == status]       
     
       
    if stage  != "":  
       list_of_filters=[p for p in list_of_filters if p.stage == stage]        
    
     
    if gender != "": 
       list_of_filters=[p for p in list_of_filters if p.Gender == gender]       
       
    if  gender  == "" and stage  == "" and status  == "" and job_id  == "":
        list_of_filters=CandidateQueries.get_candidates_of_all_jobs();

    
    
    return list_of_filters;
    


@router.get('/{job_id}')
def get_candidates_of_jobs(job_id):
    candidates=CandidateQueries.get_candidates_of_job_by_id(job_id);
    return candidates;

@router.post('/')
async def add_candidate (request: Request): 
    candidate =await request.json()
    new_candidate=CandidateQueries.add_candidate_user(candidate)
    return new_candidate;



    
    
