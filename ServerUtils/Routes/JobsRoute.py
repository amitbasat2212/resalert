from fastapi import APIRouter,Request

from ServerUtils.queries import JobsQueries;



router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)


@router.get('/')
def get_open_jobs():
    open_jobs=JobsQueries.get_open_jobs();
    return open_jobs;
       

@router.post('/')
async def add_job (request: Request):
    job =await request.json()
    new_job = JobsQueries.add_job(job);
    return new_job;

    
    
@router.delete('/')
def delete_job(job_id):   
    delete_job = JobsQueries.delete_job(job_id);
    return delete_job;
    