from traceback import print_tb
from ServerUtils.TypesOfObject import Status
from ServerUtils.DataBaseConnection import DataBaseManager
from fastapi.responses import JSONResponse

def get_the_new_order_status(status_old):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            query_order_old_status = f"SELECT s_order from status where s_name='{status_old}';"
            cursor.execute(query_order_old_status)
            result_status_old = cursor.fetchall()
            new_status_order = result_status_old[0]["s_order"]+1
            return new_status_order;

    except TypeError as e:
        return e



def get_new_status(candidate_id,job_id):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            query_old_status = f"SELECT status from person_jobs where candidante_id='{candidate_id}' AND job_id={job_id};"
            cursor.execute(query_old_status)
            result_status = cursor.fetchall()
            new_status_order=get_the_new_order_status(result_status[0]["status"])           
            if new_status_order < 11:
                new_status = get_new_status_name(new_status_order)
                return new_status
            return 0;
    except TypeError as e:
        return e


def get_new_status_name(s_order_new):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            query_next_status = f"SELECT s_name from status where s_order='{s_order_new}';"
            cursor.execute(query_next_status)
            result_status = cursor.fetchall()
            new_status = result_status[0]["s_name"]
            return new_status

    except TypeError as e:
        return e


def update_status_of_job_of_candidate(candidate_email, job_id):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            new_status = get_new_status(candidate_email,job_id)
            if(new_status==0):
                     return JSONResponse(
                        status_code=400,
                        content={"message":f"this is the last status"},
                        ) 
            update_status_of_person_in_job = f"UPDATE person_jobs SET status='{new_status}' WHERE candidante_id='{candidate_email}' AND job_id='{job_id}'"
            cursor.execute(update_status_of_person_in_job)
            DataBaseManager.connection.commit()
            return {"succes": 200}

    except TypeError as e:
        return e
