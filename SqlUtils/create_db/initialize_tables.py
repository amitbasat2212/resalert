import pymysql
from ServerUtils.TypesOfObject.parser import parse

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


if __name__ == "__main__":
    candidates, open_jobs, person_jobs, statuses, final_stages, departements = parse("SqlUtils/utils/person_jobs.json")
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="res_alert",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor,
    )
    init_table(connection, "pokemons", pokemons)
    init_table(connection, "trainers", trainers)
    init_table(connection, "pokemons_trainers", pokemons_trainers)
    init_table(connection, "types", types)
    init_table(connection, "pokemons_types", pokemons_types)
