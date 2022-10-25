
from fastapi import APIRouter
from ServerUtils.queries import StatusQueries;
from ServerUtils.queries import StageQueries;


router = APIRouter(
    prefix="/PersonJobs",
    tags=["PersonJobs"]
)

@router.put('/status')
def update_the_status_of_candidate_job(candidate_email,job_id,status_name):
    update_status=StatusQueries.update_status_of_job_of_candidate(candidate_email,job_id,status_name)
    return update_status;

@router.put('/stages')
def update_the_stage_of_candidate_job(candidate_email,job_id,stages_name):
    update_stage=StageQueries.update_the_final_stage(candidate_email,job_id,stages_name)
    return update_stage;




