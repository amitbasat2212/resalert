from unittest import result
from ServerUtils.DataBaseConnection import DataBaseManager
from ServerUtils.TypesOfObject import PersonJobs
from ServerUtils.TypesOfObject import Candidate


def create_candidates(candidates):
    candidates_of_jobs = []
    for candidate in candidates:
        candidates_of_jobs.append(create_candidate(candidate))
    return candidates_of_jobs


def create_candidate(candidate):
    new_candidate = (PersonJobs.PersonJobs(candidate["c_first_name"], candidate["c_last_name"], candidate["c_mail"], candidate["c_cv"],
                                           candidate["job_name"],
                                           candidate["oj_id"],
                                           candidate["status"],
                                           candidate["final_stage"],
                                           candidate["c_gender"])
                     )
    return new_candidate


def get_candidates_of_all_jobs():
    candidates_of_jobs = []
    try:
        with DataBaseManager.connection.cursor() as cursor:
            query_candidates_of_jobs = f"SELECT * from person_jobs as pe,open_jobs as oj,candidates as ca WHERE ca.c_mail=pe.candidante_id AND oj.oj_id=pe.job_id;"
            cursor.execute(query_candidates_of_jobs)
            result_candidates = cursor.fetchall()
            candidates_of_jobs = create_candidates(result_candidates)
            return candidates_of_jobs

    except TypeError as e:
        return e


def create_person(candidate_user):
    new_candidate_person = (Candidate.Candidate(candidate_user["c_first_name"], candidate_user["c_last_name"],
                                                candidate_user["c_mail"],
                                                candidate_user["c_cv"],
                                                candidate_user["c_gender"]))
    return new_candidate_person


def add_candidate_to_a_job(candidate_mail, job_id):
    status = "CV unread"
    stage = "pending"
    try:
        with DataBaseManager.connection.cursor() as cursor:
            insert_candidate_user = f"INSERT IGNORE INTO person_jobs values('{candidate_mail}','{job_id}','{status}','{stage}')"
            cursor.execute(insert_candidate_user)
            DataBaseManager.connection.commit()
            return {"candidate_mail": candidate_mail, "job_id": job_id, "status": status, "stage": stage}
    except TypeError as e:
        return e


def add_candidate_user(candidate):
    try:
        with DataBaseManager.connection.cursor() as cursor:
            insert_candidate_user = f"INSERT IGNORE INTO candidates values('{candidate.f_name}','{candidate.l_name}','{candidate.mail}','{candidate.cv}','{candidate.Gender}')"
            cursor.execute(insert_candidate_user)
            DataBaseManager.connection.commit()
            new_candidate_user = create_person(candidate)
            return new_candidate_user
    except TypeError as e:
        return e
