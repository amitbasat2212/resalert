from fastapi import APIRouter



router = APIRouter(
    prefix="/PersonJobs",
    tags=["PersonJobs"]
)

@router.put('/status')
def update_the_status_of_candidate_job(candidate_email,job_id,status_name):
    pass;


@router.put('/stages')
def update_the_stage_of_candidate_job(candidate_email,job_id,stages_name):
    pass;




