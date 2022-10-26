from ServerUtils.TypesOfObject import FinalStage
from ServerUtils.DataBaseConnection import DataBaseManager;



def update_the_final_stage(candidate_email,job_id,stage_name):
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            update_stage_of_person_in_job = f"UPDATE person_jobs SET final_stage={stage_name} WHERE candidate_mail={candidate_email} AND job={job_id}"
            cursor.execute(update_stage_of_person_in_job)  
            DataBaseManager.connection.commit()         
            return {"succes":200};          
   
    except TypeError as e:
        return e;