
from fastapi import APIRouter
from ServerUtils.queries import StatusQueries
from ServerUtils.queries import StageQueries


router = APIRouter(
    prefix="/personjobs",
    tags=["personjobs"]
)


@router.put('/status')
async def update_the_status_of_candidate_job(candidate_id, job_id):
    update_status = StatusQueries.update_status_of_job_of_candidate(
        candidate_id, job_id)
    return update_status


   
@router.put('/stages')
async def update_the_stage_of_candidate_job(candidate_id, job_id, stage):
    update_stage = StageQueries.update_the_final_stage(
        candidate_id, job_id, stage)
    return update_stage
