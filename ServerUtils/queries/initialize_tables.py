from ServerUtils.DataBaseConnection import DataBaseManager
from ServerUtils.TypesOfObject import parser


def init_table(connection, table_name, data):
    try:
        with connection.cursor() as cursor:
            query = f"""
                    INSERT INTO {table_name} VALUES
                    {",".join([str(e) for e in data])}
                    """
            cursor.execute(query)
            connection.commit()
    except Exception as e:
        print(f"Error in initializing {table_name} table")
        print(e)


def init_the_database():
    candidates, open_jobs, person_jobs, statuses, final_stages, departements = parser.parse(
        "SqlUtils/utils/person_jobs.json")
    connection = DataBaseManager.connection
    init_table(connection, "candidates", candidates)
    #init_table(connection, "departements", departements)
    #init_table(connection, "final_stage", final_stages)
    # init_table(connection, "open_jobs", open_jobs)
    # init_table(connection, "person_jobs", person_jobs)
    # init_table(connection, "status", statuses)
