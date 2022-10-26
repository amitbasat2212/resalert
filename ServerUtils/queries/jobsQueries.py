from ServerUtils.TypesOfObject import OpenJob
from ServerUtils.DataBaseConnection import DataBaseManager;

def create_open_jobs(jobs):
    open_jobs=[]
    for job in jobs:
        open_jobs.append(create_open_job(job))
    return open_jobs;    
        

def create_open_job(job):
   open_job= OpenJob.OpenJob(job["oj_id"],
        job["job_name"],
        job["department_name"]);
   return open_job;     


def get_open_jobs():
    open_jobs  =[];
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            query_open_jobs = f"SELECT * from open_jobs;"
            cursor.execute(query_open_jobs)            
            result_open_jobs = cursor.fetchall()                                 
            open_jobs=create_open_jobs(result_open_jobs);
            return open_jobs;           
   
    except TypeError as e:
        return e;



def add_job(open_job):  
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            insert_new_job = f"INSERT IGNORE INTO open_jobs values('{open_job['oj_id']}','{open_job['job_name']}','{open_job['department_name']}')"
            cursor.execute(insert_new_job)
            DataBaseManager.connection.commit()                              
            new_open_job=create_open_job(open_job);
            return new_open_job;  
    except TypeError as e:
        return e;



def find_job_by_id(job_id):
    try:
        with DataBaseManager.connection.cursor() as cursor:            
            query_excist_job = f"SELECT * from open_jobs where oj_id='{job_id}';"
            cursor.execute(query_excist_job)            
            result_job= cursor.fetchall()                                 
            if(len(result_job)==0):
                return False;
            return True;            
   
    except TypeError as e:
        return e;


def delete_from_tables(job_id,table,param):
    try:
        with DataBaseManager.connection.cursor() as cursor: 
            if_row_excist = find_job_by_id(job_id)           
            if(if_row_excist):
                delete_candidate_of_jobs= f"Delete from {table} where {param}='{job_id}';"
                cursor.execute(delete_candidate_of_jobs)               
                DataBaseManager.connection.commit()
                return {"succes":200}            
            return {}

   
    except TypeError as e:
        return e;


def delete_from_person_jobs(job_id):
    delete_from_tables(job_id,"person_jobs","job_id");

def delete_from_open_jobs(job_id): 
    delete_from_tables(job_id,"open_jobs","oj_id")


def delete_job(job_id): 
    try:
        with DataBaseManager.connection.cursor() as cursor: 
            if_row_excist = find_job_by_id(job_id)           
            if(if_row_excist):                
                delete_from_person_jobs(job_id)
                delete_from_open_jobs(job_id)
                return {"succes":200}            
            return {}

   
    except TypeError as e:
        return e;