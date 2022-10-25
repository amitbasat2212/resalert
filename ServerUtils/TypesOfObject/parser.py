import json
from ServerUtils.TypesOfObject import Candidate
from ServerUtils.TypesOfObject import Departements
from ServerUtils.TypesOfObject import FinalStage
from ServerUtils.TypesOfObject import OpenJob
from ServerUtils.TypesOfObject import JobByPerson
from ServerUtils.TypesOfObject import Status


def _get_dict_from_json(json_dir: str):
    person_jobs_data_file = open(json_dir)
    person_jobs_data = json.load(person_jobs_data_file)
    person_jobs_data_file.close()
    return person_jobs_data


def _parse_person_jobs_data(person_jobs_data):
    candidates, open_jobs, person_jobs, statuses, final_stages, departements = set(
    ), set(), set(), set(), set(), set()
    person_jobs_data = person_jobs_data[0]
    # print(departements)
    for d in person_jobs_data["departements"]:
        dep = Departements.Departements((d["dep_name"]))
        departements.add(dep)

    for fj in person_jobs_data["final_stage"]:
        final_stage = FinalStage.FinalStage(fj["fs_name"])
        final_stages.add(final_stage)

    for s in person_jobs_data["status"]:
        status = Status.Status(s["s_order"], s["s_name"])
        statuses.add(status)

    for c in person_jobs_data["candidates"]:
        candidate = Candidate.Candidate(
            c["c_first_name"], c["c_last_name"], c["c_mail"], c["c_cv"], c["c_gender"])
        candidates.add(candidate)

    for op in person_jobs_data["open_jobs"]:
        open_job = OpenJob.OpenJob(
            op["oj_id"], op["job_name"], op["department_name"])
        open_jobs.add(open_job)

    for pj in person_jobs_data["person_jobs"]:
        person_job = JobByPerson.JobByPerson(
            pj["candidante_id"], pj["job_id"], pj["status"], pj["finsl_stage"])
        person_jobs.add(person_job)

    return candidates, open_jobs, person_jobs, statuses, final_stages, departements


def parse(json_dir: str):
    person_jobs_data = _get_dict_from_json(json_dir)
    return _parse_person_jobs_data(person_jobs_data)


# print(parse("SqlUtils/utils/person_jobs.json"))
