from ServerUtils.TypesOfObject import OpenJob
from ServerUtils.DataBaseConnection import DataBaseManager;


def get_numberes_per_gender():
   try:
        with DataBaseManager.connection.cursor() as cursor:
            query_boys_vs_girls = f"SELECT COUNT(c_mail) as num_candidate,c_gender from candidates GROUP BY c_gender"
            cursor.execute(query_boys_vs_girls)
            result_boys_vs_girls = cursor.fetchall()
            return result_boys_vs_girls;
   except TypeError as e:
        return e 


def get_emploes_per_department():
   try:
        with DataBaseManager.connection.cursor() as cursor:
            query_empoloy_per_dep = f"SELECT COUNT(candidante_id) as member,de.dep_name from person_jobs as pj,departements as de, open_jobs as oj WHERE de.dep_name=oj.department_name AND pj.job_id=oj_id GROUP BY de.dep_name"
            cursor.execute(query_empoloy_per_dep)
            result_employ_per_dep = cursor.fetchall()
            return result_employ_per_dep;
   except TypeError as e:
        return e


