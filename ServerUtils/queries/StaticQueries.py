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
            query_boys_vs_girls = f"SELECT COUNT() from person_jobs as pj,departments as de, open_jobs as oj WHERE  GROUP BY de.dep_name"
            cursor.execute(query_boys_vs_girls)
            result_boys_vs_girls = cursor.fetchall()
            return result_boys_vs_girls;
   except TypeError as e:
        return e


