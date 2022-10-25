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
            insert_new_job = f"""INSERT IGNORE INTO open_jobs values('{open_job["id"]}',
            '{open_job["name"]}',
            '{open_job["dep_name"]}'"""
            cursor.execute(insert_new_job)
            DataBaseManager.connection.commit()                              
            new_open_job=create_open_job(open_job);
            return new_open_job;  
    except TypeError as e:
        return e;