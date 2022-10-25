from fastapi import APIRouter


from ServerUtils.TypesOfObject import OpenJob


router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)


@router.get('/')
def get_open_jobs():
   
    pass

@router.post('/')
def add_job (job):
    new_job = OpenJob(job.job_open_id,job.job_name,job.dep_name);


    return new_job;
    
    
@router.delete('/')
def delete_job(job_id):
   
    pass