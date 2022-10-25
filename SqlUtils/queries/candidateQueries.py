from unittest import result
from SqlUtils.DataBaseConnection import DataBaseManager;
from ServerUtils.TypesOfObject import Candidate
from ServerUtils.TypesOfObject import Person

def create_candidates(candidates):
    candidates_of_jobs=[]
    for candidate in candidates:
        candidates_of_jobs.append(Candidate.Candiddate(candidate["c_first_name"],candidate["c_last_name"],
        candidate["c_mail"],
        candidate["c_cv"],
        candidate["job"],
        candidate["status"],
        candidate["final_stage"]))

    return candidates_of_jobs;    
        




def create_candedate(candidate):
    new_candidate=(Candidate.Candiddate(candidate["c_first_name"],candidate["c_last_name"],
        candidate["c_mail"],
        candidate["c_cv"],
        candidate["job"],
        candidate["status"],
        candidate["final_stage"]))
    return new_candidate   



def add_candidate(candidate):
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            insert_candidate = f"""INSERT IGNORE INTO candidates values('{candidate["f_name"]}',
            '{candidate["l_name"]}',
            '{candidate["email"]}',
            '{candidate["cv"]}',
            '{candidate["Gender"]}'"""
            cursor.execute(insert_candidate)
            DataBaseManager.connection.commit()                              
            new_candidate=create_candedate(candidate);
            return new_candidate;  
    except TypeError as e:
        return e;

  




def get_candidates_of_jobs(job_id):
    candidates_of_jobs=[]
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            query_candidates_of_jobs = f"SELECT * from person_jobs where job ={job_id}  ;"
            cursor.execute(query_candidates_of_jobs)            
            result_candidates = cursor.fetchall()                                 
            candidates_of_jobs=create_candidates(result_candidates);
            return candidates_of_jobs;
            
   
    except TypeError as e:
        return e;



    