from unittest import result
from SqlUtils.DataBaseConnection import DataBaseManager;
def create_candidates(candidates):
    candidates_of_jobs=[]
    for candidate in candidates:
        candidates_of_jobs.append(candidate["c_first_name"],candidate["c_last_name"],
        candidate["c_mail"],
        candidate["c_cv"],
        candidate["job"],
        candidate["status"],
        candidate["final_stage"])
        



def get_candidates_of_jobs(job_id):
    # candidates_of_jobs=[]
    # try:
    #     with DataBaseManager.connection.cursor() as cursor:            
    #         query_candidates_of_jobs = f"SELECT * from person_jobs where job ={job_id}  ;"
    #         cursor.execute(query_candidates_of_jobs)            
    #         result_candidates = cursor.fetchall()                                 
    #         candidates_of_jobs=create_candidates(result_candidates);
    #         return candidates_of_jobs;
            
   
    # except TypeError as e:
    #     return e;

    return True;
