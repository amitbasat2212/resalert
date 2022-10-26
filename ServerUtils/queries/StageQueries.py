from ServerUtils.TypesOfObject import FinalStage
from ServerUtils.DataBaseConnection import DataBaseManager


<<<<<<< HEAD
def check_is_stage_in_db(stage_name):
=======

def update_the_final_stage(candidate_email,job_id,stage_name):
>>>>>>> 4d5cb5c10ec11dcc0f23e79ebc455ec84b956909
    try:
        with DataBaseManager.connection.cursor() as cursor:
            query_next_status = f"SELECT fs_name from final_stage where fs_name='{stage_name}';"
            cursor.execute(query_next_status)
            result_stage = cursor.fetchall()
            return stage_name == result_stage[0]["fs_name"]
    except TypeError as e:
        return e

def update_the_final_stage(candidate_email, job_id, stage_name):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            if check_is_stage_in_db(stage_name):
                update_stage_of_person_in_job = f"UPDATE person_jobs SET final_stage='{stage_name}' WHERE candidante_id='{candidate_email}' AND job_id='{job_id}'"
                cursor.execute(update_stage_of_person_in_job)
                DataBaseManager.connection.commit()
                return {"succes": 200}

    except TypeError as e:
        return e
