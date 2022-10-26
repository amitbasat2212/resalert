from traceback import print_tb
from ServerUtils.TypesOfObject import Status
from ServerUtils.DataBaseConnection import DataBaseManager


def get_new_status_order(status_name):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            query_next_status = f"SELECT s_order from status where s_name='{status_name}';"
            cursor.execute(query_next_status)
            result_status = cursor.fetchall()
            new_status_order = result_status[0]["s_order"]+1
            if new_status_order < 11:
                new_status = get_new_status_name(new_status_order)
                return new_status

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


def update_status_of_job_of_candidate(candidate_email, job_id, status_name):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            new_status = get_new_status_order(status_name)
            update_status_of_person_in_job = f"UPDATE person_jobs SET status='{new_status}' WHERE candidante_id='{candidate_email}' AND job_id='{job_id}'"
            cursor.execute(update_status_of_person_in_job)
            DataBaseManager.connection.commit()
            return {"succes": 200}

    except TypeError as e:
        return e
