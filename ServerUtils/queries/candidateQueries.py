from unittest import result
from  ServerUtils.DataBaseConnection import DataBaseManager;
from ServerUtils.TypesOfObject import PersonJobs
from ServerUtils.TypesOfObject import Candidate

def create_candidates(candidates):
    candidates_of_jobs=[]
    for candidate in candidates:
        candidates_of_jobs.append(create_candidate(candidate))
    return candidates_of_jobs;    
 
def create_candidate(candidate):
    new_candidate=(PersonJobs.PersonJobs(candidate["c_first_name"],candidate["c_last_name"],
        candidate["c_mail"],
        candidate["c_cv"],
        candidate["job"],
        candidate["status"],
        candidate["final_stage"]))
    return new_candidate   

def get_candidates_of_job_by_id(job_id):
    candidates_of_jobs=[]
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            query_candidates_of_jobs = f"SELECT * from person_jobs as pe,candidates as ca WHERE ca.c_mail=pe.candidate_mail AND job ={job_id}  ;"
            cursor.execute(query_candidates_of_jobs)            
            result_candidates = cursor.fetchall()                                 
            candidates_of_jobs=create_candidates(result_candidates);
            return candidates_of_jobs;
            
   
    except TypeError as e:
        return e;


def get_candidates_of_all_jobs():
    candidates_of_jobs=[]
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            query_candidates_of_jobs = f"SELECT * from person_jobs as pe,candidates as ca WHERE ca.c_mail=pe.candidate_mail;"
            cursor.execute(query_candidates_of_jobs)            
            result_candidates = cursor.fetchall()                                 
            candidates_of_jobs=create_candidates(result_candidates);
            return candidates_of_jobs;
            
   
    except TypeError as e:
        return e;




def create_person(candidate_user):
    new_candidate_person=(Candidate.Candidate(candidate_user["c_first_name"],candidate_user["c_last_name"],
        candidate_user["c_mail"],
        candidate_user["c_cv"],
        candidate_user["c_gender"]))
    return new_candidate_person 

def add_candidate_user(candidate):
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            insert_candidate_user = f"""INSERT IGNORE INTO candidates values('{candidate["f_name"]}',
            '{candidate["l_name"]}',
            '{candidate["email"]}',
            '{candidate["cv"]}',
            '{candidate["Gender"]}'"""
            cursor.execute(insert_candidate_user)
            DataBaseManager.connection.commit()                              
            new_candidate_user=create_person(candidate);
            return new_candidate_user;  
    except TypeError as e:
        return e;

  




