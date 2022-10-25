from fastapi import APIRouter

from SqlUtils.queries import jobsQueries;
from ServerUtils.TypesOfObject import OpenJob



router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)


@router.get('/')
def get_open_jobs():
    open_jobs=jobsQueries.get_open_jobs();
    return open_jobs;
       

@router.post('/')
def add_job (job):
    # new_job = OpenJob(job.job_open_id,job.job_name,job.dep_name);
    # return new_job;
    pass;
    
    
@router.delete('/')
def delete_job(job_id):   
    pass